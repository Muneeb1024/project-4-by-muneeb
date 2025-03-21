# Problem Statement.
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

# Import the random library 
import random



print("\nSimulates rolling two dice and prints their total")
print("_" * 55, "\n")



# Global constant: Number of sides on each die.
NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    return die1, die2, die1 + die2  # Return values instead of printing



def main():
    rolls = 3  # Number of rolls (can be modified for scalability)
    
    print("🎲 Rolling the dice... 🎲\n")
    
    for i in range(1, rolls + 1):
        die1, die2, total = roll_dice()
        print(f"Roll {i}: 🎲 {die1} + 🎲 {die2} = {total}")

    print("\n🎉 Simulation Complete! 🎉\n")

# Run the program
if __name__ == '__main__':
    main()


