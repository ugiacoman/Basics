# CS 141 lab 5
# encrypt.py
#
# Modified by: Ulises Giacoman
#
# This program will prompt the user for a message and shift. Using the
# message and shift, the program will encypt your message. 

shift = int(input("Please enter shift: "))
print(shift)

message = input("Please enter your message: ")
print(message)
length_of_message = len(message)

for index in range(0, length_of_message):
    
    char = message[index]
    if char.islower():
        char = ord(char) - ord("a")
        char = (char + shift) % 26
        char = chr(char + ord("a"))
        print(char, end = "")
    else:
        print(char, end = "")