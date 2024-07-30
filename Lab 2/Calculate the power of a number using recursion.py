def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

# Example usage:
base, exponent = 2, 3
print(f"{base} to the power of {exponent}: {power(base, exponent)}")
