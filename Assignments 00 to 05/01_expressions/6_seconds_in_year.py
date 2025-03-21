# Print a welcome message
print("\n🎲 This program calculates the number of seconds in a year")
print("_" * 60, "\n")

def calculate_seconds(year_type: str):
    """
    Function to calculate the total number of seconds in a given year type.
    """
    # Constants for time conversion
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    # Determine the number of days based on the year type
    days = 365 if year_type == "normal" else 366  # Using a compact if-else

    # Calculate total seconds
    total_seconds = SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY * days

    # Print the result
    print(f"\nA {year_type} year has {total_seconds} seconds.\n")

def main():
    """
    Main function to get valid user input and call the calculation function.
    """
    while True:
        year_type = input("Choose year type (normal/leap): ").strip().lower()
        
        # Validate input
        if year_type in ["normal", "leap"]:
            calculate_seconds(year_type)
            break  # Exit the loop after a valid input
        else:
            print("❌ Invalid input! Please enter 'normal' or 'leap'. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
