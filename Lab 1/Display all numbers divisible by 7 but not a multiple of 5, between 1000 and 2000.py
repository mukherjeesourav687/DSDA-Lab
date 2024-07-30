def divisible_by_7_not_5():
    result = [i for i in range(1000, 2001) if i % 7 == 0 and i % 5 != 0]
    return result

# Example usage:
print(f"Numbers divisible by 7 but not by 5 between 1000 and 2000: {divisible_by_7_not_5()}")
