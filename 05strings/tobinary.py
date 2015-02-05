# CS 141 lab 5
# tobinary.py
#
# Modified by: Ulises Giacoman
#
# This program will prompt the user for a postive integer. It will then convert
# the positive integer to a binary string.

pos_int = int(input("Please enter a postive integer value: "))
print(pos_int)

number = ""

if pos_int == 0:
    print("Binary string is:", pos_int)
else:
    while pos_int > 0:
        binary = pos_int % 2
        if binary == 0:
            number = "O" + number
        elif binary == 1: 
            number = "1" + number
        pos_int = pos_int // 2
        
    print("Binary string is:", number)