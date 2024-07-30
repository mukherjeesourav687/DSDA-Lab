def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Example usage:
arr = [1, 2, 3, 4, 5]
print(f"Reversed array: {reverse_list(arr)}")
