"""
Optimized 3-body simulation.

Optimizations vs. main.py:
  1. Numba @njit on the ODE right-hand side (the function is called thousands
     of times by the integrator -- this is by far the biggest win).
  2. Replace np.linalg.norm(d) ** 3 with (dx*dx + dy*dy + dz*dz) ** -1.5
     (no sqrt, no temporary arrays).
  3. Use Newton's third law: pairwise displacement is computed once and
     reused for both bodies (F_ij = -F_ji).
  4. Pre-allocate the output array; no per-call np.array(...).ravel().
  5. DOP853 integrator (higher order -> fewer RHS evaluations for the same
     tolerance vs. the default RK45).
  6. Multiprocessing pool to run perturbed initial conditions in parallel,
     visualizing the chaotic divergence inherent to the 3-body problem.

Run modes:
    python main_optimized.py             # single run + benchmark vs. original
    python main_optimized.py --parallel  # parallel multi-trajectory run
"""

from __future__ import annotations

import argparse
import time
from multiprocessing import Pool, cpu_count

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

try:
    from numba import njit

    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False

    def njit(*args, **kwargs):  # graceful fallback if numba isn't installed
        if len(args) == 1 and callable(args[0]):
            return args[0]

        def deco(f):
            return f

        return deco


# ------------------------------------------------------------------- #
# Initial conditions
# ------------------------------------------------------------------- #

M1, M2, M3 = 1.0, 1.0, 1.0

INITIAL_CONDITIONS = np.array(
    [
        # positions
        -0.5, 0.0, 0.0,
        0.5, 0.0, 0.0,
        0.0, 0.001, 1.0,
        # velocities
        0.0, 0.347111, 0.0,
        0.0, -0.347111, 0.0,
        0.0, 0.0, -0.1,
    ],
    dtype=np.float64,
)

TIME_START, TIME_END = 0.0, 7.0
N_POINTS = 2001


# ------------------------------------------------------------------- #
# Hot path: ODE right-hand side (Numba-compiled)
# ------------------------------------------------------------------- #

@njit(cache=True, fastmath=True)
def system_odes_fast(t, S, m1, m2, m3):
    p1x, p1y, p1z = S[0], S[1], S[2]
    p2x, p2y, p2z = S[3], S[4], S[5]
    p3x, p3y, p3z = S[6], S[7], S[8]
    v1x, v1y, v1z = S[9], S[10], S[11]
    v2x, v2y, v2z = S[12], S[13], S[14]
    v3x, v3y, v3z = S[15], S[16], S[17]

    # Pairwise displacements (each one only computed ONCE).
    r12x = p2x - p1x; r12y = p2y - p1y; r12z = p2z - p1z
    r13x = p3x - p1x; r13y = p3y - p1y; r13z = p3z - p1z
    r23x = p3x - p2x; r23y = p3y - p2y; r23z = p3z - p2z

    # 1 / |r|^3, no sqrt.
    inv_d12_3 = (r12x * r12x + r12y * r12y + r12z * r12z) ** -1.5
    inv_d13_3 = (r13x * r13x + r13y * r13y + r13z * r13z) ** -1.5
    inv_d23_3 = (r23x * r23x + r23y * r23y + r23z * r23z) ** -1.5

    # Accelerations -- F_ij is reused as -F_ji.
    a1x = m2 * r12x * inv_d12_3 + m3 * r13x * inv_d13_3
    a1y = m2 * r12y * inv_d12_3 + m3 * r13y * inv_d13_3
    a1z = m2 * r12z * inv_d12_3 + m3 * r13z * inv_d13_3

    a2x = -m1 * r12x * inv_d12_3 + m3 * r23x * inv_d23_3
    a2y = -m1 * r12y * inv_d12_3 + m3 * r23y * inv_d23_3
    a2z = -m1 * r12z * inv_d12_3 + m3 * r23z * inv_d23_3

    a3x = -m1 * r13x * inv_d13_3 - m2 * r23x * inv_d23_3
    a3y = -m1 * r13y * inv_d13_3 - m2 * r23y * inv_d23_3
    a3z = -m1 * r13z * inv_d13_3 - m2 * r23z * inv_d23_3

    out = np.empty(18)
    out[0], out[1], out[2] = v1x, v1y, v1z
    out[3], out[4], out[5] = v2x, v2y, v2z
    out[6], out[7], out[8] = v3x, v3y, v3z
    out[9], out[10], out[11] = a1x, a1y, a1z
    out[12], out[13], out[14] = a2x, a2y, a2z
    out[15], out[16], out[17] = a3x, a3y, a3z
    return out


# Reference implementation (same shape as the original main.py) -- kept here
# strictly so we can benchmark the speedup head-to-head.
def system_odes_reference(t, S, m1, m2, m3):
    p1, p2, p3 = S[0:3], S[3:6], S[6:9]
    dp1_dt, dp2_dt, dp3_dt = S[9:12], S[12:15], S[15:18]
    f1, f2, f3 = dp1_dt, dp2_dt, dp3_dt
    df1_dt = (
        m3 * (p3 - p1) / np.linalg.norm(p3 - p1) ** 3
        + m2 * (p2 - p1) / np.linalg.norm(p2 - p1) ** 3
    )
    df2_dt = (
        m3 * (p3 - p2) / np.linalg.norm(p3 - p2) ** 3
        + m1 * (p1 - p2) / np.linalg.norm(p1 - p2) ** 3
    )
    df3_dt = (
        m1 * (p1 - p3) / np.linalg.norm(p1 - p3) ** 3
        + m2 * (p2 - p3) / np.linalg.norm(p2 - p3) ** 3
    )
    return np.array([f1, f2, f3, df1_dt, df2_dt, df3_dt]).ravel()


# ------------------------------------------------------------------- #
# Custom Numba-jitted integrators (bypass scipy entirely)
# ------------------------------------------------------------------- #

@njit(cache=True, fastmath=True)
def rk4_integrate(y0, t_eval, m1, m2, m3, substeps):
    """Fixed-step RK4 over a uniform t_eval grid.

    Each output interval is divided into `substeps` internal RK4 steps so
    accuracy can be tightened without changing the output grid.
    """
    n_out = t_eval.size
    n_dim = y0.size
    out = np.empty((n_dim, n_out))
    for d in range(n_dim):
        out[d, 0] = y0[d]

    y = y0.copy()
    for i in range(1, n_out):
        h = (t_eval[i] - t_eval[i - 1]) / substeps
        t = t_eval[i - 1]
        for _ in range(substeps):
            k1 = system_odes_fast(t, y, m1, m2, m3)
            k2 = system_odes_fast(t + 0.5 * h, y + 0.5 * h * k1, m1, m2, m3)
            k3 = system_odes_fast(t + 0.5 * h, y + 0.5 * h * k2, m1, m2, m3)
            k4 = system_odes_fast(t + h, y + h * k3, m1, m2, m3)
            y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
            t = t + h
        for d in range(n_dim):
            out[d, i] = y[d]
    return out


# Dormand-Prince (DOPRI5) coefficients -- module-level so numba folds them in.
_A21 = 1.0 / 5.0
_A31 = 3.0 / 40.0;       _A32 = 9.0 / 40.0
_A41 = 44.0 / 45.0;      _A42 = -56.0 / 15.0;     _A43 = 32.0 / 9.0
_A51 = 19372.0 / 6561.0; _A52 = -25360.0 / 2187.0
_A53 = 64448.0 / 6561.0; _A54 = -212.0 / 729.0
_A61 = 9017.0 / 3168.0;  _A62 = -355.0 / 33.0
_A63 = 46732.0 / 5247.0; _A64 = 49.0 / 176.0;     _A65 = -5103.0 / 18656.0

_B1 = 35.0 / 384.0;  _B3 = 500.0 / 1113.0
_B4 = 125.0 / 192.0; _B5 = -2187.0 / 6784.0; _B6 = 11.0 / 84.0

# E_i = B_i - B_hat_i  (5th-order minus 4th-order embedded estimate)
_E1 = 71.0 / 57600.0;     _E3 = -71.0 / 16695.0
_E4 = 71.0 / 1920.0;      _E5 = -17253.0 / 339200.0
_E6 = 22.0 / 525.0;       _E7 = -1.0 / 40.0


@njit(cache=True, fastmath=True)
def rk45_integrate(y0, t_eval, m1, m2, m3, rtol, atol):
    """Adaptive Dormand-Prince (RK45) integrator with FSAL.

    Output is recorded at each t_eval point by capping the step size so it
    lands exactly on the boundary. Step rejection follows the standard
    safety/min/max factor scheme used by scipy.
    """
    n_out = t_eval.size
    n_dim = y0.size
    out = np.empty((n_dim, n_out))
    for d in range(n_dim):
        out[d, 0] = y0[d]

    y = y0.copy()
    t = t_eval[0]
    t_end = t_eval[-1]

    span = t_end - t
    h = span * 0.01
    h_min = 1e-12
    h_max = span
    safety = 0.9
    min_factor = 0.2
    max_factor = 10.0

    k1 = system_odes_fast(t, y, m1, m2, m3)  # FSAL: reused across accepted steps
    next_out = 1
    n_steps = 0
    n_rejected = 0

    while next_out < n_out:
        h_step = h
        if t + h_step > t_eval[next_out]:
            h_step = t_eval[next_out] - t
        if h_step > h_max:
            h_step = h_max
        if h_step < h_min:
            h_step = h_min

        k2 = system_odes_fast(t + h_step * 0.2,
                              y + h_step * (_A21 * k1), m1, m2, m3)
        k3 = system_odes_fast(t + h_step * 0.3,
                              y + h_step * (_A31 * k1 + _A32 * k2), m1, m2, m3)
        k4 = system_odes_fast(t + h_step * 0.8,
                              y + h_step * (_A41 * k1 + _A42 * k2 + _A43 * k3), m1, m2, m3)
        k5 = system_odes_fast(t + h_step * (8.0 / 9.0),
                              y + h_step * (_A51 * k1 + _A52 * k2 + _A53 * k3 + _A54 * k4),
                              m1, m2, m3)
        k6 = system_odes_fast(t + h_step,
                              y + h_step * (_A61 * k1 + _A62 * k2 + _A63 * k3
                                            + _A64 * k4 + _A65 * k5),
                              m1, m2, m3)
        y_new = y + h_step * (_B1 * k1 + _B3 * k3 + _B4 * k4 + _B5 * k5 + _B6 * k6)
        k7 = system_odes_fast(t + h_step, y_new, m1, m2, m3)

        # Error norm (scipy convention: RMS of err / scale)
        err_sq = 0.0
        for j in range(n_dim):
            e = h_step * (_E1 * k1[j] + _E3 * k3[j] + _E4 * k4[j]
                          + _E5 * k5[j] + _E6 * k6[j] + _E7 * k7[j])
            sc = atol + rtol * max(abs(y[j]), abs(y_new[j]))
            err_sq += (e / sc) ** 2
        err_norm = (err_sq / n_dim) ** 0.5

        if err_norm < 1.0:
            t = t + h_step
            y = y_new
            k1 = k7  # FSAL
            n_steps += 1

            while next_out < n_out and t >= t_eval[next_out] - 1e-14:
                for d in range(n_dim):
                    out[d, next_out] = y[d]
                next_out += 1

            if err_norm == 0.0:
                factor = max_factor
            else:
                factor = safety * err_norm ** (-0.2)
                if factor > max_factor:
                    factor = max_factor
                elif factor < min_factor:
                    factor = min_factor
            h = h_step * factor
        else:
            n_rejected += 1
            factor = safety * err_norm ** (-0.2)
            if factor < min_factor:
                factor = min_factor
            h = h_step * factor

    return out


# ------------------------------------------------------------------- #
# Solver wrappers
# ------------------------------------------------------------------- #

def solve(y0, t_eval, method="DOP853", fast=True, rtol=1e-3, atol=1e-6):
    rhs = system_odes_fast if fast else system_odes_reference
    return solve_ivp(
        fun=rhs,
        t_span=(t_eval[0], t_eval[-1]),
        y0=y0,
        t_eval=t_eval,
        method=method,
        args=(M1, M2, M3),
        rtol=rtol,
        atol=atol,
    )


def _solve_worker(y0):
    """Top-level so it's picklable for multiprocessing.Pool."""
    t_eval = np.linspace(TIME_START, TIME_END, N_POINTS)
    sol = solve(y0, t_eval, fast=True)
    return sol.y


# ------------------------------------------------------------------- #
# Benchmark
# ------------------------------------------------------------------- #

def _time_solve(t_eval, **kwargs):
    # First call may include numba compilation; second call is the steady-state.
    solve(INITIAL_CONDITIONS, t_eval, **kwargs)
    t0 = time.perf_counter()
    sol = solve(INITIAL_CONDITIONS, t_eval, **kwargs)
    return sol, time.perf_counter() - t0


def _verify_rhs_equivalence():
    """Confirm fast and reference RHS produce identical outputs (modulo FP noise).

    This is the only meaningful correctness check: comparing endpoints of two
    chaotic integrations is dominated by chaos, not by RHS accuracy.
    """
    rng = np.random.default_rng(42)
    max_err = 0.0
    for _ in range(50):
        S = INITIAL_CONDITIONS + 0.1 * rng.standard_normal(18)
        a = system_odes_fast(0.0, S, M1, M2, M3)
        b = system_odes_reference(0.0, S, M1, M2, M3)
        max_err = max(max_err, float(np.max(np.abs(a - b))))
    return max_err


def benchmark(t_eval):
    print(f"Numba available: {HAS_NUMBA}")
    if not HAS_NUMBA:
        print("  -> install with `uv pip install numba` for the real speedup")
    print()

    # Warm up the JIT.
    if HAS_NUMBA:
        system_odes_fast(0.0, INITIAL_CONDITIONS, M1, M2, M3)

    rhs_err = _verify_rhs_equivalence()
    print(f"RHS equivalence check (max abs diff over 50 random states): {rhs_err:.2e}")
    print()

    print("== Default tolerance (rtol=1e-3, atol=1e-6) -- matches main.py ==")
    _, t_orig = _time_solve(t_eval=t_eval, fast=False, method="RK45")
    sol_fast, t_fast = _time_solve(t_eval=t_eval, fast=True, method="DOP853")
    print(f"  RK45  + Python RHS:  {t_orig*1000:7.2f} ms")
    print(f"  DOP853+ fast RHS:    {t_fast*1000:7.2f} ms   ({t_orig/t_fast:.2f}x)")
    print()

    print("== Strict tolerance (rtol=atol=1e-9) -- high-precision regime ==")
    sol_ref, t_orig_s = _time_solve(t_eval=t_eval, fast=False, method="RK45",
                                    rtol=1e-9, atol=1e-9)
    sol_fast_s, t_fast_s = _time_solve(t_eval=t_eval, fast=True, method="DOP853",
                                       rtol=1e-9, atol=1e-9)
    print(f"  RK45  + Python RHS:  {t_orig_s*1000:7.2f} ms")
    print(f"  DOP853+ fast RHS:    {t_fast_s*1000:7.2f} ms   ({t_orig_s/t_fast_s:.2f}x)")
    print()

    # At strict tolerance, both solvers are converged to ~1e-9, so endpoint
    # comparison is meaningful (chaos hasn't blown up below the tolerance floor).
    converged_drift = np.max(np.abs(sol_fast_s.y[:, -1] - sol_ref.y[:, -1]))
    print(f"Converged endpoint drift (strict tol): {converged_drift:.2e}")
    print()

    # ------------------------------------------------------------- #
    # Custom Numba-jitted integrators (no scipy in the hot loop).
    # ------------------------------------------------------------- #
    print("== Custom Numba integrators (no scipy overhead) ==")

    # Warm up JITs.
    _ = rk4_integrate(INITIAL_CONDITIONS, t_eval, M1, M2, M3, 1)
    _ = rk45_integrate(INITIAL_CONDITIONS, t_eval, M1, M2, M3, 1e-3, 1e-6)

    # Reference: scipy DOP853 at strict tolerance (gold standard).
    gold = sol_ref.y[:, -1]

    for substeps in (1, 4, 16):
        t0 = time.perf_counter()
        for _ in range(2):
            y_rk4 = rk4_integrate(INITIAL_CONDITIONS, t_eval, M1, M2, M3, substeps)
        t_rk4 = (time.perf_counter() - t0) / 2
        err = np.max(np.abs(y_rk4[:, -1] - gold))
        print(f"  RK4 (substeps={substeps:>2}):       {t_rk4*1000:7.2f} ms"
              f"   err vs gold: {err:.2e}")

    for rtol, atol in ((1e-3, 1e-6), (1e-9, 1e-9)):
        t0 = time.perf_counter()
        for _ in range(2):
            y_rk45 = rk45_integrate(INITIAL_CONDITIONS, t_eval, M1, M2, M3, rtol, atol)
        t_rk45 = (time.perf_counter() - t0) / 2
        err = np.max(np.abs(y_rk45[:, -1] - gold))
        print(f"  RK45 (rtol={rtol:.0e}):       {t_rk45*1000:7.2f} ms"
              f"   err vs gold: {err:.2e}")

    print()
    original_ms = t_orig * 1000
    print(f"Original main.py baseline (RK45 + Python RHS, default tol): {original_ms:.2f} ms")
    return sol_fast


# ------------------------------------------------------------------- #
# Plotting
# ------------------------------------------------------------------- #

def animate_single(sol, t_eval):
    p1x, p1y, p1z = sol.y[0], sol.y[1], sol.y[2]
    p2x, p2y, p2z = sol.y[3], sol.y[4], sol.y[5]
    p3x, p3y, p3z = sol.y[6], sol.y[7], sol.y[8]

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    (planet1_plt,) = ax.plot(p1x, p1y, p1z, "green", label="Planet 1", linewidth=1)
    (planet2_plt,) = ax.plot(p2x, p2y, p2z, "red", label="Planet 2", linewidth=1)
    (planet3_plt,) = ax.plot(p3x, p3y, p3z, "blue", label="Planet 3", linewidth=1)

    (planet1_dot,) = ax.plot([p1x[-1]], [p1y[-1]], [p1z[-1]], "o", color="green", markersize=6)
    (planet2_dot,) = ax.plot([p2x[-1]], [p2y[-1]], [p2z[-1]], "o", color="red", markersize=6)
    (planet3_dot,) = ax.plot([p3x[-1]], [p3y[-1]], [p3z[-1]], "o", color="blue", markersize=6)

    ax.set_title("The 3-Body Problem (optimized)")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
    plt.legend()

    def update(frame):
        lo = max(0, frame - 300)
        for plt_line, dot, x, y, z in (
            (planet1_plt, planet1_dot, p1x, p1y, p1z),
            (planet2_plt, planet2_dot, p2x, p2y, p2z),
            (planet3_plt, planet3_dot, p3x, p3y, p3z),
        ):
            plt_line.set_data(x[lo:frame + 1], y[lo:frame + 1])
            plt_line.set_3d_properties(z[lo:frame + 1])
            dot.set_data([x[frame]], [y[frame]])
            dot.set_3d_properties([z[frame]])
        return planet1_plt, planet1_dot, planet2_plt, planet2_dot, planet3_plt, planet3_dot

    _ = FuncAnimation(fig, update, frames=range(0, len(t_eval), 2), interval=10, blit=True)
    plt.show()


def run_parallel(n_runs=8, perturbation=1e-6):
    """Run n_runs perturbed trajectories in parallel and overlay them."""
    rng = np.random.default_rng(0)
    y0_batch = [
        INITIAL_CONDITIONS + perturbation * rng.standard_normal(INITIAL_CONDITIONS.size)
        for _ in range(n_runs)
    ]
    y0_batch[0] = INITIAL_CONDITIONS  # keep one unperturbed reference

    workers = min(n_runs, cpu_count())
    print(f"Running {n_runs} trajectories on {workers} workers (perturbation={perturbation:g})...")
    t0 = time.perf_counter()
    with Pool(workers) as pool:
        trajectories = pool.map(_solve_worker, y0_batch)
    print(f"Parallel solve: {time.perf_counter() - t0:.3f} s")

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    cmap = plt.get_cmap("viridis")
    for i, y in enumerate(trajectories):
        c = cmap(i / max(1, n_runs - 1))
        ax.plot(y[0], y[1], y[2], color=c, linewidth=0.6, alpha=0.8)
        ax.plot(y[3], y[4], y[5], color=c, linewidth=0.6, alpha=0.8)
        ax.plot(y[6], y[7], y[8], color=c, linewidth=0.6, alpha=0.8)
    ax.set_title(f"3-Body chaos: {n_runs} perturbed trajectories")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
    plt.show()


# ------------------------------------------------------------------- #
# Entry point
# ------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parallel", action="store_true",
                        help="Run perturbed trajectories in parallel (chaos demo)")
    parser.add_argument("--runs", type=int, default=8,
                        help="Number of parallel trajectories (with --parallel)")
    parser.add_argument("--no-anim", action="store_true",
                        help="Skip the matplotlib animation (benchmark only)")
    args = parser.parse_args()

    t_eval = np.linspace(TIME_START, TIME_END, N_POINTS)

    if args.parallel:
        run_parallel(n_runs=args.runs)
        return

    sol = benchmark(t_eval)
    if not args.no_anim:
        animate_single(sol, t_eval)


if __name__ == "__main__":
    main()
