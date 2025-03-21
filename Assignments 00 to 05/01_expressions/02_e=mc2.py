# Problem Statement
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2




print("\nThis Python program calculates energy using Einstein’s famous equation:")
print("_" * 90 ,"\n")

C = 299792458  # The speed of light in m/s

mass: float = float(input("Enter kilos of mass: "))

e = mass * (C ** 2)


# Display work to the user
print("\ne = m * C^2...")
print(f"m = {mass}kg")
print(f"C = {C}m/s\n")
    
print(f"{e} joules of energy!\n")

