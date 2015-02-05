# CS141 lab 6
# studentroster.py
#
# Modified by: Ulises Giacoman
#
# A program that takes a text document and turns it into a roster. 



students = open("students.txt", "r")
roster = open("roster.txt", "w")
file_line = students.readline()
print(students)

studentClass = ""
studentName = ""
studentGpa = ""
studentAverageGpa = 0
count = 0

roster.write("%4s %21s %9s" % ("Name", "Class", "GPA\n"))
roster.write("-" * 37)
roster.write("\n")

while file_line != "":
    count = count + 1
    studentName = students.readline().rstrip()
    studentGpa = students.readline().rstrip()
    studentClass = students.readline().rstrip()
    
    if int(studentClass) == 1:
        studentClass = "Freshman"
    elif int(studentClass) == 2:
        studentClass = "Sophomore"
    elif int(studentClass) == 3:
        studentyear = "Junior"
    elif int(studentClass) == 4:
        studentClass = "Senior"
    elif int(studentClass) == 5:
        studentClass = "not available"
        
    studentAverageGpa = (float(studentGpa) + studentAverageGpa)
    roster.write("%-20s %-10s %-9s \n" % (studentName, studentClass, studentGpa))
    file_line = students.readline()
    
studentAverageGpa = studentAverageGpa / count
roster.write("-" * 37)
roster.write("\n")
roster.write("%11s %23.2f " % ("Average GPA:", studentAverageGpa))

roster.close() 
    
    