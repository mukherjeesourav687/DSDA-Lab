def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Example usage:
base = 2
exponent = 3
print(f"{base} to the power of {exponent}: {power(base, exponent)}")
