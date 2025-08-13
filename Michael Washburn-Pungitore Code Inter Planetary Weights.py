# Named Constants for surface gravity factors
GRAVITY_MERCURY = 0.38
GRAVITY_VENUS = 0.91
GRAVITY_MOON = 0.165
GRAVITY_MARS = 0.38
GRAVITY_JUPITER = 2.34
GRAVITY_SATURN = 0.93
GRAVITY_URANUS = 0.92
GRAVITY_NEPTUNE = 1.12
GRAVITY_PLUTO = 0.066

# Prompt user for name and Earth weight
s_Name = input("What is your name? ")
s_Weight = input("What is your weight? ")

# Convert weight to float
n_Weight = float(s_Weight)

# Output header
print()
print("Here is your weight on our Solar System's planets:")
print()

# Calculate and print formatted weights on each planet
print("Weight on Mercury: {:10.2f}".format(n_Weight * GRAVITY_MERCURY))
print("Weight on Venus:   {:10.2f}".format(n_Weight * GRAVITY_VENUS))
print("Weight on Moon:    {:10.2f}".format(n_Weight * GRAVITY_MOON))
print("Weight on Mars:    {:10.2f}".format(n_Weight * GRAVITY_MARS))
print("Weight on Jupiter: {:10.2f}".format(n_Weight * GRAVITY_JUPITER))
print("Weight on Saturn:  {:10.2f}".format(n_Weight * GRAVITY_SATURN))
print("Weight on Uranus:  {:10.2f}".format(n_Weight * GRAVITY_URANUS))
print("Weight on Neptune: {:10.2f}".format(n_Weight * GRAVITY_NEPTUNE))
print("Weight on Pluto:   {:10.2f}".format(n_Weight * GRAVITY_PLUTO))
