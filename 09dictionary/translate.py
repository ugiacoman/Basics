# CS 141 Lab 9
# translate.py
# Modified by Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu

fileAbbv = open("textabbv.txt", "r")
line = fileAbbv.readline()
abbvDict = {}

sent = input("Please input sentence: ")
print(sent)
sent = sent.split()

while line != '':
    key = line.strip('\n')
    value = (fileAbbv.readline().strip('\n'))
    abbvDict[key.strip()] = value
    line = fileAbbv.readline()
    
print()
for word in sent:
    if word in abbvDict:
        print(abbvDict[word] + ' ', end= '')
    else:
        print(word + ' ', end= '')
        
fileAbbv.close()