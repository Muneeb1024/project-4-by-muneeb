import math


print("\nThis program output the hypotenuse of the right triangle")
print("_" * 90 ,"\n")

try:
# Get the two side lengths from the user and cast them to be numbers
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
except ValueError:
    print("Invalid Input\n")
else:
    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is: {bc}.\n")




