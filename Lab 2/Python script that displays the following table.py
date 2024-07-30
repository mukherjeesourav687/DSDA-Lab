def print_table(n):
    for i in range(1, n + 1):
        for j in range(1, 5):
            print(i**j, end=" ")
        print()

# Example usage:
n = 5
print_table(n)
