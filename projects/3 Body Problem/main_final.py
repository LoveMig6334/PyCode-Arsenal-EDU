import time

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from numba import njit

# ------------------------------------------------------------------- #

m1 = 1.0
m2 = 1.0
m3 = 1.0

# Position
inital_position_1 = [-0.5, 0.0, 0.0]
inital_position_2 = [0.5, 0.0, 0.0]
inital_position_3 = [0.0, 0.001, 1.0]

# Velocity
inital_velocity_1 = [0.0, 0.347111, 0]
inital_velocity_2 = [0.0, -0.347111, 0.0]
inital_velocity_3 = [0.0, 0.0, -0.1]

initial_conditions = np.array(
    [
        inital_position_1,
        inital_position_2,
        inital_position_3,
        inital_velocity_1,
        inital_velocity_2,
        inital_velocity_3,
    ],
    dtype=np.float64,
).ravel()

# ------------------------------------------------------------------- #


@njit(cache=True, fastmath=True)
def system_odes(t, S, m1, m2, m3):
    p1x, p1y, p1z = S[0], S[1], S[2]
    p2x, p2y, p2z = S[3], S[4], S[5]
    p3x, p3y, p3z = S[6], S[7], S[8]
    v1x, v1y, v1z = S[9], S[10], S[11]
    v2x, v2y, v2z = S[12], S[13], S[14]
    v3x, v3y, v3z = S[15], S[16], S[17]

    r12x = p2x - p1x
    r12y = p2y - p1y
    r12z = p2z - p1z
    r13x = p3x - p1x
    r13y = p3y - p1y
    r13z = p3z - p1z
    r23x = p3x - p2x
    r23y = p3y - p2y
    r23z = p3z - p2z

    inv_d12_3 = (r12x * r12x + r12y * r12y + r12z * r12z) ** -1.5
    inv_d13_3 = (r13x * r13x + r13y * r13y + r13z * r13z) ** -1.5
    inv_d23_3 = (r23x * r23x + r23y * r23y + r23z * r23z) ** -1.5

    out = np.empty(18)
    out[0] = v1x
    out[1] = v1y
    out[2] = v1z
    out[3] = v2x
    out[4] = v2y
    out[5] = v2z
    out[6] = v3x
    out[7] = v3y
    out[8] = v3z

    out[9] = m2 * r12x * inv_d12_3 + m3 * r13x * inv_d13_3
    out[10] = m2 * r12y * inv_d12_3 + m3 * r13y * inv_d13_3
    out[11] = m2 * r12z * inv_d12_3 + m3 * r13z * inv_d13_3

    out[12] = -m1 * r12x * inv_d12_3 + m3 * r23x * inv_d23_3
    out[13] = -m1 * r12y * inv_d12_3 + m3 * r23y * inv_d23_3
    out[14] = -m1 * r12z * inv_d12_3 + m3 * r23z * inv_d23_3

    out[15] = -m1 * r13x * inv_d13_3 - m2 * r23x * inv_d23_3
    out[16] = -m1 * r13y * inv_d13_3 - m2 * r23y * inv_d23_3
    out[17] = -m1 * r13z * inv_d13_3 - m2 * r23z * inv_d23_3
    return out


# Dormand-Prince (DOPRI5) coefficients
_A21 = 1.0 / 5.0
_A31 = 3.0 / 40.0
_A32 = 9.0 / 40.0
_A41 = 44.0 / 45.0
_A42 = -56.0 / 15.0
_A43 = 32.0 / 9.0
_A51 = 19372.0 / 6561.0
_A52 = -25360.0 / 2187.0
_A53 = 64448.0 / 6561.0
_A54 = -212.0 / 729.0
_A61 = 9017.0 / 3168.0
_A62 = -355.0 / 33.0
_A63 = 46732.0 / 5247.0
_A64 = 49.0 / 176.0
_A65 = -5103.0 / 18656.0

_B1 = 35.0 / 384.0
_B3 = 500.0 / 1113.0
_B4 = 125.0 / 192.0
_B5 = -2187.0 / 6784.0
_B6 = 11.0 / 84.0

_E1 = 71.0 / 57600.0
_E3 = -71.0 / 16695.0
_E4 = 71.0 / 1920.0
_E5 = -17253.0 / 339200.0
_E6 = 22.0 / 525.0
_E7 = -1.0 / 40.0


@njit(cache=True, fastmath=True)
def rk45_integrate(y0, t_eval, m1, m2, m3, rtol, atol):
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

    k1 = system_odes(t, y, m1, m2, m3)
    next_out = 1

    while next_out < n_out:
        h_step = h
        if t + h_step > t_eval[next_out]:
            h_step = t_eval[next_out] - t
        if h_step > h_max:
            h_step = h_max
        if h_step < h_min:
            h_step = h_min

        k2 = system_odes(t + h_step * 0.2, y + h_step * (_A21 * k1), m1, m2, m3)
        k3 = system_odes(
            t + h_step * 0.3, y + h_step * (_A31 * k1 + _A32 * k2), m1, m2, m3
        )
        k4 = system_odes(
            t + h_step * 0.8,
            y + h_step * (_A41 * k1 + _A42 * k2 + _A43 * k3),
            m1,
            m2,
            m3,
        )
        k5 = system_odes(
            t + h_step * (8.0 / 9.0),
            y + h_step * (_A51 * k1 + _A52 * k2 + _A53 * k3 + _A54 * k4),
            m1,
            m2,
            m3,
        )
        k6 = system_odes(
            t + h_step,
            y + h_step * (_A61 * k1 + _A62 * k2 + _A63 * k3 + _A64 * k4 + _A65 * k5),
            m1,
            m2,
            m3,
        )
        y_new = y + h_step * (_B1 * k1 + _B3 * k3 + _B4 * k4 + _B5 * k5 + _B6 * k6)
        k7 = system_odes(t + h_step, y_new, m1, m2, m3)

        err_sq = 0.0
        for j in range(n_dim):
            e = h_step * (
                _E1 * k1[j]
                + _E3 * k3[j]
                + _E4 * k4[j]
                + _E5 * k5[j]
                + _E6 * k6[j]
                + _E7 * k7[j]
            )
            sc = atol + rtol * max(abs(y[j]), abs(y_new[j]))
            err_sq += (e / sc) ** 2
        err_norm = (err_sq / n_dim) ** 0.5

        if err_norm < 1.0:
            t = t + h_step
            y = y_new
            k1 = k7
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
            factor = safety * err_norm ** (-0.2)
            if factor < min_factor:
                factor = min_factor
            h = h_step * factor

    return out


# Trigger Numba compilation outside the timed region.
_warmup_t = np.linspace(0.0, 1e-3, 2)
rk45_integrate(initial_conditions, _warmup_t, m1, m2, m3, 1e-3, 1e-6)

# ------------------------------------------------------------------- #


time_s, time_e = 0, 7
t_points = np.linspace(time_s, time_e, 2001)

t1 = time.perf_counter()
y_sol = rk45_integrate(initial_conditions, t_points, m1, m2, m3, 1e-3, 1e-6)
t2 = time.perf_counter()
print(f"Solved in: {t2 - t1:.5f} [s]")


t_sol = t_points
p1x_sol = y_sol[0]
p1y_sol = y_sol[1]
p1z_sol = y_sol[2]

p2x_sol = y_sol[3]
p2y_sol = y_sol[4]
p2z_sol = y_sol[5]

p3x_sol = y_sol[6]
p3y_sol = y_sol[7]
p3z_sol = y_sol[8]

# ------------------------------------------------------------------- #

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

(planet1_plt,) = ax.plot(
    p1x_sol, p1y_sol, p1z_sol, "green", label="Planet 1", linewidth=1
)
(planet2_plt,) = ax.plot(
    p2x_sol, p2y_sol, p2z_sol, "red", label="Planet 2", linewidth=1
)
(planet3_plt,) = ax.plot(
    p3x_sol, p3y_sol, p3z_sol, "blue", label="Planet 3", linewidth=1
)

(planet1_dot,) = ax.plot(
    [p1x_sol[-1]], [p1y_sol[-1]], [p1z_sol[-1]], "o", color="green", markersize=6
)
(planet2_dot,) = ax.plot(
    [p2x_sol[-1]], [p2y_sol[-1]], [p2z_sol[-1]], "o", color="red", markersize=6
)
(planet3_dot,) = ax.plot(
    [p3x_sol[-1]], [p3y_sol[-1]], [p3z_sol[-1]], "o", color="blue", markersize=6
)


ax.set_title("The 3-Body Problem")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.grid()
plt.legend()


def update(frame):
    lower_lim = max(0, frame - 300)
    print(f"Progress: {(frame + 1) / len(t_points):.1%} | 100.0 %", end="\r")

    x_current_1 = p1x_sol[lower_lim : frame + 1]
    y_current_1 = p1y_sol[lower_lim : frame + 1]
    z_current_1 = p1z_sol[lower_lim : frame + 1]

    x_current_2 = p2x_sol[lower_lim : frame + 1]
    y_current_2 = p2y_sol[lower_lim : frame + 1]
    z_current_2 = p2z_sol[lower_lim : frame + 1]

    x_current_3 = p3x_sol[lower_lim : frame + 1]
    y_current_3 = p3y_sol[lower_lim : frame + 1]
    z_current_3 = p3z_sol[lower_lim : frame + 1]

    planet1_plt.set_data(x_current_1, y_current_1)
    planet1_plt.set_3d_properties(z_current_1)

    planet1_dot.set_data([x_current_1[-1]], [y_current_1[-1]])
    planet1_dot.set_3d_properties([z_current_1[-1]])

    planet2_plt.set_data(x_current_2, y_current_2)
    planet2_plt.set_3d_properties(z_current_2)

    planet2_dot.set_data([x_current_2[-1]], [y_current_2[-1]])
    planet2_dot.set_3d_properties([z_current_2[-1]])

    planet3_plt.set_data(x_current_3, y_current_3)
    planet3_plt.set_3d_properties(z_current_3)

    planet3_dot.set_data([x_current_3[-1]], [y_current_3[-1]])
    planet3_dot.set_3d_properties([z_current_3[-1]])

    return planet1_plt, planet1_dot, planet2_plt, planet2_dot, planet3_plt, planet3_dot


animation = FuncAnimation(
    fig, update, frames=range(0, len(t_points), 2), interval=10, blit=True
)
plt.show()
