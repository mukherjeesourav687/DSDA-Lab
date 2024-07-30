def find_factors(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

# Example usage:
number = 28
print(f"Factors of {number} are {find_factors(number)}")
