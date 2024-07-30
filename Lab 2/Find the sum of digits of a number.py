def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
number = 1234
print(f"Sum of digits of {number}: {sum_of_digits(number)}")
