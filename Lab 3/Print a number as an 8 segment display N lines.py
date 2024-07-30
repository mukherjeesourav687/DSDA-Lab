def print_8_segment(n):
    for i in range(n):
        print(" _  ", end="")
    print()

    for i in range(n):
        print("|_| ", end="")
    print()

    for i in range(n):
        print("|_| ", end="")
    print()

# Example usage:
n = 4
print_8_segment(n)
