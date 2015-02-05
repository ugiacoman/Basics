# CS 141 lab 2
# cylinder.py
#
# Modified by: Ulises Giacoman
#
# This program calculates the volume, surface area and circumference of
# a cylinder with values for the radius and height provided by the user

import math

# Prompts and converts to float the radius and height of the cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the circumference of cylinder
circum = 2 * math.pi * radius

# Calculate the surface area of cylinder
surfArea = 2 * math.pi * radius * height

# Calculate the volume of cylinder
volume = math.pi * (radius ** 2) * height

# Display the results on the screen
print(" The circumference is", circum)
print(" The surface area is", surfArea)
print(" The volume is", volume)