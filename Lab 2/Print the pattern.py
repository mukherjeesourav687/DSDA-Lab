def print_pattern(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
        if i % 2 == 0:
            num -= i * 2

# Example usage:
n = 4
print_pattern(n)
