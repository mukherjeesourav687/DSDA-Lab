def geometric_sequence(a, r, n):
    sequence = [a * r**i for i in range(n)]
    return sequence

# Example usage:
a = 2
r = 3
n = 6
print(f"First {n} terms of geometric sequence: {geometric_sequence(a, r, n)}")
