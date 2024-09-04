import numpy as np

# Function to compute cost
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X @ theta
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

# Function to perform gradient descent
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    cost_history = np.zeros(iterations)

    for i in range(iterations):
        gradient = (1 / m) * (X.T @ (X @ theta - y))
        theta -= learning_rate * gradient
        cost_history[i] = compute_cost(X, y, theta)

    return theta, cost_history

# Sample data
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]])  # Add intercept term
y = np.array([2, 4, 5, 4, 5]).reshape(-1, 1)
theta = np.zeros((2, 1))

# Perform gradient descent
learning_rate = 0.01
iterations = 1000
theta, cost_history = gradient_descent(X, y, theta, learning_rate, iterations)

print("Optimised coefficients:", theta.ravel())
