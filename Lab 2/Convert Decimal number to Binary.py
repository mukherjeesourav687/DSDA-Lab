def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# Example usage:
n = 10
print(f"Binary of {n}: {decimal_to_binary(n)}")
