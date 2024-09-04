import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Add a column of ones to X to represent the intercept term
X = np.vstack((np.ones(len(X)), X)).T

# Compute coefficients using the normal equation
coefficients = np.linalg.inv(X.T @ X) @ X.T @ y

# Plot data and regression line
plt.scatter(X[:, 1], y, color='red', label='Data points')
plt.plot(X[:, 1], X @ coefficients, color='blue', label='Regression Line')
plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
