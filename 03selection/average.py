# CS 141 Lab 3
# average.py 
#
# Modified by: Ulises Giacoman
#
# This program asks the user to enter three grades
# the program then reads these grades and calculate the average
# After the program computers the average it outputs a letter grade. 


grade1 = int(input(" Please input the 1st grade: "))
grade2 = int(input(" Please input the 2nd grade: "))
grade3 = int(input(" Please input the 3rd grade: "))
    
average= (grade1 + grade2 + grade3) / 3
print(" Average score = ", round(average))
#round function is to round the input to the nearest integer.

print(" The student", end= "" )
if average >= 90.0:
    print(" passed and got an A.")
elif average >= 80.0:
    print(" passed and got a B.")
elif average >= 70.0:
    print(" passed and got a C.")
elif average >= 60.0:
    print(" passed and got a D.")
else:
    print(" failed and got a F.")