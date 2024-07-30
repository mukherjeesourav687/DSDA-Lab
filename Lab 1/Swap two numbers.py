def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Example usage:
a = 5
b = 10
a, b = swap_numbers(a, b)
print(f"Swapped numbers: a = {a}, b = {b}")
