# CS 141 lab 2
# line.py
#
# Modified by: Ulises Giacoman
#
# This program calculates the length of a line segment
# defined by two Cartisian coordinates (x0,y0) and (x1, y1)
# Then it calculates the slope. 
import math

# Prompt and convert to integer the two points that define the line.
x0IntStr = input("Enter the x-coordinate for the first point: ")
x0 = int(x0IntStr)

y0IntStr = input("Enter the y-coordinate for the first point: ")
y0 = int(y0IntStr)

x1IntStr = input("Enter the x-coordinate for the second point: ")
x1 = int(x1IntStr)

y1IntStr = input("Enter the y-coordinate for the second point: ")
y1 = int(y1IntStr)

# Calculate the length of the line over the x- and y-axes.
base = x1 - x0 
height = y1 - y0 

# Calculate the length of the line itself.
length = math.sqrt(base ** 2 + height ** 2)

# Display the result on the screen.
print("The length of the line is", length)


# Calculate slope of the line
slope = (height / base)

# Display the result on the screen
print("The slope of the line is", slope)