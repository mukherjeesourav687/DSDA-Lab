import math

def sin_series(x, n):
    sin_x = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)
        sin_x += term
    return sin_x

# Example usage:
x = math.radians(30)  # Convert degrees to radians
n = 10
print(f"sin({x}) using series up to {n} terms: {sin_series(x, n)}")
