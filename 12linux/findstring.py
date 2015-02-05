# CS 141 lab 12
# findstring.py
#
# Modified by:
#
# This program takes a word and a file from the user
# and displays the location of the first occurence of a word in a line.

import sys
import string

def main():
    word = input("Enter string to be found: ")
    filename = input("Enter filename: ")

    fileHandle = open(filename, "r")
    findAll(word, fileHandle)
    
##########You do not need to modify anything in this function ############

def findAll(search, fh):
    count = 0
    found = False
    for line in fh:
        pos = -1
        count += 1
        words = line.split()
        if words.count(search) > 0:
            pos = words.index(search) 
        if pos != -1:
            found = True
            print("Found",search,"as word",pos+1,"in line",count)
    if not found:
        print("The file does not contain the word",search)
    	
##########################################################################

main()

