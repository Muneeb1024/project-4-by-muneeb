# Problem Statement
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).


print("\n\nThis program print the sum of all side length of the triangle")
print("_" * 65, "\n")


try:
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 1? "))
    side3 = float(input("What is the length of side 1? "))
except ValueError:
    print("Invalid Input, Input must be a number.")
else:
    print(f"\nThe perimeter of the triangle is {side1 + side2 + side3}.\n")



