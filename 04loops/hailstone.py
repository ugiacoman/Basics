# CS 141 Lab 3
# hailstone.py 
#
# Modified by: Ulises Giacoman
#
# This program calculates the hailstone sequence and then exits out if the
# integer is 1.

arbitrary_int = float(input("Please enter integer: "))
print(arbitrary_int, end= ' ')

while arbitrary_int != 1:
    if arbitrary_int % 2 == 0:
        arbitrary_int /= 2
        print(arbitrary_int, end= ' ')
    elif arbitrary_int % 2 != 0:
        arbitrary_int = (arbitrary_int * 3) + 1
        print(arbitrary_int, end= ' ')
    else:
        print()