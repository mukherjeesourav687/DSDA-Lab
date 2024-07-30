import math

def cos_series(x, n):
    cos_x = 0
    for i in range(n):
        term = ((-1)**i * x**(2*i)) / math.factorial(2*i)
        cos_x += term
    return cos_x

# Example usage:
x = math.radians(30)  # Convert degrees to radians
n = 10
print(f"cos({x}) using series up to {n} terms: {cos_series(x, n)}")
