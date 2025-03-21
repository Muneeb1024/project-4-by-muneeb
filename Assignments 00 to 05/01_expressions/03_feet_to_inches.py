# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.



print("\nThis program convert feet to inches ")
print("_" * 90 ,"\n")


inches_in_foot = 12
try:
    foot = float(input("Enter number of Feet: "))
except ValueError:
    print("Invalid Input, Please enter a number.\n")
else:
    result = foot * inches_in_foot
    print(f"\nThe Converted Value is {foot}feet to inches is {result}inches\n")







