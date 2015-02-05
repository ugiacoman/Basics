# CS 141 lab 12
# args.py
#
# This program is meant to show how to integrate the use of command-line 
# arguments into a Python program. It takes a filename as a command-line 
# argument and counts to number of words (separated by spaces) contained
# in that file.

# The system library is needed in order to access the special list
# named argv.
import sys 

# The program expects to receive one argument and since the command is 
# always the first element in the list, the size of sys.argv should be at 
# least 2. If not, we know that the user failed to supply a filename.
# and the program can not run since it doesn't know what file to use.
if len(sys.argv) < 2:
    print("Error: No file name provided.")
    sys.exit()  # allows us to immediately exit the program.

# For this example, we don't care if there are more than 2 items in the 
# argv list since we only need the item at index one and can ignore all 
# the rest.

# We get the filename from the first element of the list and open the 
# file. We also use a try/except block to catch an exception in case
# the file can not be opened.
fileName = sys.argv[1]

try:
    theFile = open(fileName)
	
  # An IOError exception will occure if the file can not be opened. 
except IOError:
    print("The file %s can not be opened or does not exist", fileName)
    sys.exit()
	
# A filename was provided and we were able to open it. Now, we extract the
# text and count the number of words contained in the file.

count = 0 #initialize the word count to 0
for line in theFile :
    wordList = line.split()
    count += len(wordList)
	
print("The number of words in the file is", count)
	












