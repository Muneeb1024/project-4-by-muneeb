# Problem Statement:
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).



print("\n\nThis program print Favourite Animal")
print("_" * 35, "\n")

try:
    user_animal = input("What's your favorite animal? ")
    if user_animal.isdigit():
        raise ValueError("Input Must be a string, not a number.")
except ValueError as er:
    print(f"Error: {er}")
else:
    print(f"My favourite animal is also {user_animal}!\n")        
