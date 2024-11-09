#Q2:- Write a program that will convert celsius value to fahrenheit.

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Conversion
fahrenheit = celsius_to_fahrenheit(celsius)

# Output the result
print(f"{celsius}°C is equal to {fahrenheit}°F")
