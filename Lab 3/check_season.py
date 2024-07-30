def check_season(month):
    if month in ['December', 'January', 'February']:
        return "Winter"
    elif month in ['March', 'April', 'May']:
        return "Spring"
    elif month in ['June', 'July', 'August']:
        return "Summer"
    elif month in ['September', 'October', 'November']:
        return "Autumn"
    else:
        return "Invalid month"

# Example usage:
month = "July"
print(f"The season in {month} is {check_season(month)}")
