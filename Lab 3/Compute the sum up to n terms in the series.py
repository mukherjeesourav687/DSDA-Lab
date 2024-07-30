def series_sum(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum -= 1/i
        else:
            sum += 1/i
    return sum

# Example usage:
n = 10
print(f"Sum of the series up to {n} terms: {series_sum(n)}")
