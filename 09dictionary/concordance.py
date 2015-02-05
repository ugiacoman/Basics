# CS 141 Lab 9
# concordance.py
# Modified by Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.

txtFile = input('Please enter filename to be read: ')
print(txtFile)

txt = open(txtFile, 'r')

concDict= {}

lineCount = 1
for line in txt:
    line = line.strip().lower().split()
    
    for indvWord in line:
        if indvWord in concDict:
            concDict[indvWord].append(lineCount)
        else:
            concDict[indvWord] = [lineCount]
    
    lineCount += 1

print()
print('---------------------------')
print('Word, Line Number')
print('---------------------------')
print('---------------------------')
for word in sorted(concDict):
    appearances = concDict[word]   
    print(word, appearances)
    
print('---------------------------')