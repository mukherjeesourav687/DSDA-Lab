import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Function to compute Gaussian distribution
def gaussian(x, mean, variance):
    return (1 / (np.sqrt(2 * np.pi * variance))) * np.exp(-((x - mean) ** 2) / (2 * variance))

# Generate values
x = np.linspace(-10, 10, 1000)

# Plot Gaussian distributions for different means and variances
plt.figure(figsize=(10, 6))
for mean in [0, 1, -2]:
    for variance in [1, 2, 4]:
        y = gaussian(x, mean, variance)
        plt.plot(x, y, label=f"mean={mean}, variance={variance}")

plt.title("Effect of Varying Mean and Variance on Gaussian Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
