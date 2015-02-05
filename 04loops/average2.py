# CS 141 Lab 3
# average.py 
#
# Modified by: Ulises Giacoman
#
# This program asks the user for their grades.
# Then the program reads these grades and calculate the average
# After the program computers the average it outputs a letter grade. 

grade_float = 0
count_int = 0
sum_float = 0

while grade_float != -1:
    
    
    grade_float = float(input("Please enter grade "))
    print(grade_float)
    count_int += 1
    sum_float = sum_float + grade_float
    
average_float = round(sum_float / (count_int - 1))    

#round function is to round the input to the nearest integer.

if average_float >= 90.0:
    print("Average grade: A")
    print("Great job! You did exceptional work.")
elif average_float >= 80.0:
    print("Average grade: B")
    print("You did above average work.")
elif average_float >= 70.0:
    print("Average grade: C")
    print("You did average work.")
elif average_float >= 60.0:
    print("Average grade: D")
    print("You marginally passed.")
else:
    print("Average grade: F")
    print("Not good! You failed.")