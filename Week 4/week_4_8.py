import matplotlib.pyplot as plt
import numpy as np


def plot_normal_distribution(mu, sigma, num_samples=1000, bins=30,
                             color='skyblue', label='Generated Data'):
    # Generate random samples from a normal distribution
    s = np.random.normal(mu, sigma, num_samples)

    # Create the histogram
    count, bins, ignored = plt.hist(
        s,
        bins=bins,
        density=True,
        color=color,
        alpha=0.6,
        label=label
    )

    # Create x values for theoretical PDF curve
    x = np.linspace(min(bins), max(bins), 100)

    # Normal distribution formula (PDF)
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * \
          np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))

    # Plot PDF curve
    plt.plot(
        x,
        pdf,
        linewidth=2,
        color='red',
        label=f'PDF (mu={mu}, sigma={sigma})'
    )

    plt.title(f'Normal Distribution: mu={mu}, sigma={sigma}')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)


# --- Task Part 1: Generate and Visualize Multiple Normal Distributions ---

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plot_normal_distribution(mu=0, sigma=1,
                         color='lightgreen',
                         label='Dist 1 Data')

plt.subplot(1, 3, 2)
plot_normal_distribution(mu=5, sigma=0.5,
                         color='salmon',
                         label='Dist 2 Data')

plt.subplot(1, 3, 3)
plot_normal_distribution(mu=-2, sigma=2,
                         color='lightblue',
                         label='Dist 3 Data')

plt.tight_layout()
plt.show()


# --- Task Part 3: Optional Challenge – Skewed Distribution ---

plt.figure(figsize=(6, 4))
skewed = np.random.exponential(scale=1, size=1000)
plt.hist(skewed, bins=30, density=True, alpha=0.6)
plt.title("Skewed Distribution (Exponential)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.show()