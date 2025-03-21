

# Print a welcome message
print("\n🎲 This program prints a fun sentence")
print("_" * 40, "\n")

SENTENCE_START: str = "GIAIC is fun. I learned to program and used Python to make my" 

def main():
    # Get the three inputs from the user to make the adlib
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(f"\n{SENTENCE_START} {adjective} {noun} {verb}!\n")




if __name__ == '__main__':
    main()