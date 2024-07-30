def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Undefined slope"
    return (y2 - y1) / (x2 - x1)

# Example usage:
x1, y1 = 1, 2
x2, y2 = 3, 4
print(f"The slope is {calculate_slope(x1, y1, x2, y2)}")
