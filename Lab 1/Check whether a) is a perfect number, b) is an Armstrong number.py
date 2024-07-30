def is_perfect_number(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

# Example usage:
number = 28
print(f"Is {number} a perfect number? {is_perfect_number(number)}")
number = 153
print(f"Is {number} an Armstrong number? {is_armstrong_number(number)}")
