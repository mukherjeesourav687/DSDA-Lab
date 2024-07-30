def factorial_series(n):
    factorial = 1
    series = []
    for i in range(1, n + 1):
        factorial *= i
        series.append(factorial)
    return series

# Example usage:
n = 6
print(f"Series up to {n} terms: {factorial_series(n)}")
