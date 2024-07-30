def fibonacci_series(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
n = 100
print(f"Fibonacci series up to {n}: {fibonacci_series(n)}")
