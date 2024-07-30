def is_palindrome(n):
    return str(n) == str(n)[::-1]

# Example usage:
number = 12321
print(f"Is {number} a palindrome? {is_palindrome(number)}")
