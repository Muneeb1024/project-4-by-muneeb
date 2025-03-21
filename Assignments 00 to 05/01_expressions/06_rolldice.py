import random



print("\n🎲 Welcome to the Dice Rolling Simulator! 🎲")
print("_" * 50,"\n")

def roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"🎲 Rolling the dice... 🎲")
    print(f"Your First die: {die1}")
    print(f"Your Second die: {die2}")
    print(f"Total of two dice is {total}.")
    return total



def main():

    roll_counts = {}  # Dictionary to store how many times each total appears

    while True:
        total = roll()
        # Update the roll count for the total
        roll_counts[total] = roll_counts.get(total, 0) + 1

        # Ask if the user wants to roll again
        choice = input("\nRoll again? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            break

    # Display statistics
    print("\n📊 Dice Roll Statistics:")
    for total, count in sorted(roll_counts.items()):
        print(f"Total {total} appeared {count} times.")

    print("\n🎲 Thanks for playing! 🎲\n")

# Run the program
if __name__ == "__main__":
    main()
