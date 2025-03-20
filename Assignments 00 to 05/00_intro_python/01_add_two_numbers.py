# Problem Statement:
# Write a Python program that takes two integer inputs from the user and calculates their sum.


print("\n\nThis Program Add Two Numbers")
print("-" * 30, "\n")

try:
    num1 = int(input("Enter number1 to perform addition: "))
    num2 = int(input("Enter number2 to perform addition: "))
except ValueError:
    print("Error: Invalid input, please enter a number.")
else:
    print(f"The total sum is {num1 + num2}.\n")


