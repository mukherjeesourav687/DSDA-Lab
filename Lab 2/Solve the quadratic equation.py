import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return "Complex roots"

# Example usage:
a, b, c = 1, -3, 2
print(f"Roots of the quadratic equation: {solve_quadratic(a, b, c)}")
