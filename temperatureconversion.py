# Temperature conversion
def convert_temperature(temp, unit):
    """This function converts temperature between Celsius and Fahrenheit"""
    unit = unit.lower()  # Accept both upper and lower case

    if unit == 'c':
        return temp * 9 / 5 + 32   # Celsius to Fahrenheit
    elif unit == 'f':
        return (temp - 32) * 5 / 9 # Fahrenheit to Celsius
    else:
        return None

print(convert_temperature(25, 'C'))  # 77.0
print(convert_temperature(25, 'F'))  # -3.888888888888889