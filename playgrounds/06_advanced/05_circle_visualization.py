import matplotlib.pyplot as plt
import numpy as np

# Parameters for the circle and the pattern
n_points = 100
multiplier = 2

# Calculate equally spaced angles (in radians) and derive circle coordinates:
angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
points = np.column_stack((np.cos(angles), np.sin(angles)))

# Set up the plot with an equal aspect ratio and no axes for a clean look
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect("equal")
ax.axis("off")

# Draw the circle outline in a vibrant color
circle_outline = plt.Circle((0, 0), 1, color="orange", fill=False, lw=3)
ax.add_artist(circle_outline)

# Prepare a list of line styles to vary the appearance of the chords
line_styles = ["solid", "dashed", "dotted", "dashdot"]

# Choose a colorful colormap for the chords (using 'rainbow' for a full spectrum effect)
colormap = plt.cm.rainbow

# Draw chords connecting points using modular multiplication:
# For each point i, we connect it to the point j = (multiplier * i) mod n_points.
for i in range(n_points):
    j = (multiplier * i) % n_points
    color = colormap(i / n_points)

    style = line_styles[i % len(line_styles)]
    lw = 0.5 + 0.5 * ((i % 3) / 2)

    if i == 0:
        ax.plot(
            [points[i, 0], points[j, 0]],
            [points[i, 1], points[j, 1]],
            color=color,
            lw=lw,
            linestyle=style,
        )
    else:
        ax.plot(
            [points[i, 0], points[j, 0]],
            [points[i, 1], points[j, 1]],
            color=color,
            lw=lw,
            linestyle=style,
        )


ax.text(
    0,
    -1.2,
    f"Modular Multiplication Circle (n={n_points}, multiplier={multiplier})",
    fontsize=16,
    ha="center",
    color="white",
)


fig.patch.set_facecolor("black")
ax.set_facecolor("black")

plt.show()
