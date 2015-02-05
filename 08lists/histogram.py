# CS141 lab 8
# histogram.py
#
# Modified by: Ulises Giacoman

print()
filename = input("Please input name of text file that contains the grades: ")
grades = open(filename, 'r')

histogram = [0] * 11

for score in grades:
    score = int(score.strip())
    histogram[score // 10] += 1

print()
print("Grade Distribution")
print("-" * 18)
print("100     : ", "*" * histogram[10])
print("90 - 99 : ", "*" * histogram[9])
print("80 - 89 : ", "*" * histogram[8])
print("70 - 79 : ", "*" * histogram[7])
print("60 - 69 : ", "*" * histogram[6])
print("50 - 59 : ", "*" * histogram[5])
print("40 - 49 : ", "*" * histogram[4])
print("30 - 39 : ", "*" * histogram[3])
print("20 - 29 : ", "*" * histogram[2])
print("10 - 19 : ", "*" * histogram[1])
print("00 - 09 : ", "*" * histogram[0])