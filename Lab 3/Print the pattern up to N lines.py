def print_pattern(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print the upper part of the triangles
        for j in range(1, i + 1):
            print("/\\", end=" ")
        print()

        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")

        # Print the lower part of the triangles
        for j in range(1, i):
            print("/__", end=" ")
        if i != 1:
            print("\\")
        else:
            print()


# Example usage:
n = 4
print_pattern(n)
