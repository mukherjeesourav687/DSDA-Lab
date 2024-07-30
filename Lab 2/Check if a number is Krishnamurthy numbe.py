import math

def is_krishnamurthy(n):
    return n == sum(math.factorial(int(digit)) for digit in str(n))

# Example usage:
number = 145
print(f"Is {number} a Krishnamurthy number? {is_krishnamurthy(number)}")
