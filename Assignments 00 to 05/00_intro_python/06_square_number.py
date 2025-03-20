# Problem Statement
# Ask the user for a number and print its square (the product of the number times itself).

print("\n\nThis program find the square of the given number")
print("_" * 40, "\n")


try:
    user_number = float(input("Type a number to see its square: "))
except ValueError:
    print("Invalid Input, Input must be a number.")
else:    
    print(f"\n\t{user_number} squared is {(user_number ** 2)}.\n")
