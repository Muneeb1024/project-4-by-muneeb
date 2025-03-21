
print("\nThis program divide the between 2 numbers with remainder")
print("_" * 60 ,"\n")


try:
   # Ask for two integers
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
except ValueError:
    print("Invalid Input\n")
else:
     # Calculate quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
     # Print the result
    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}.\n")
 

