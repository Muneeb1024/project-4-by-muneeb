# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
# formaula is to convert degree-fahrenheit to degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

print("\n\nThis program convert temperature fahrenheit to celsius.")
print("_" * 40, "\n")


try:
    user_input = float(input("Enter Temperature In Fahrenheit: "))
except ValueError:
    print("Error: Invalid input, please enter a number.")
else:
    convert = f"{(user_input - 32) * 5.0 /9.0}"
    print(f"Formula: {user_input}°F -32 * 5.0 / 9.0 = {convert}°C.\n")
    print(f"The coverted value is ({user_input}°F) to degree-celsius = {convert}°C.\n")



