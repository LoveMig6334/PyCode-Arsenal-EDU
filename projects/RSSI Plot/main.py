import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic data based on the graph in the image
distance = np.linspace(0.5, 18, 100)
rssi = -40 - 60 * np.log10(distance + 1) + np.random.normal(0, 5, size=100)

# Generate noise for the data
for i in range(len(rssi)):
    if i > 80:
        rssi[i] += np.random.normal(0, 8)
    elif i > 70:
        rssi[i] += np.random.normal(0, 7)
    elif i > 60:
        rssi[i] += np.random.normal(0, 6)
    elif i > 50:
        rssi[i] += np.random.normal(0, 5)


# Plot the data
def main() -> None:
    plt.figure(figsize=(8, 5))
    plt.scatter(
        distance,
        rssi,
        color="blue",
        label="Simulated Data",
        alpha=0.5,
        marker="x",
    )
    plt.plot(
        distance,
        -40 - 60 * np.log10(distance + 1),
        color="black",
        label="Trendline",
        alpha=0.7,
        linestyle="solid",
    )
    plt.axhline(
        y=-88,
        color="red",
        label="-88 dBm threshold",
        alpha=0.7,
        linestyle="--",
    )

    # Add labels, title, and legend
    plt.title("RSSI vs Distance")
    plt.xlabel("Distance (m)")
    plt.ylabel("RSSI (dBm)")

    plt.grid(linestyle="--", alpha=0.6, color="gray", linewidth=0.8)
    plt.xlim(0, 20)
    plt.ylim(-140, -30)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
