# CS 141 Lab 10
# testline.py
#
# A program that tests the line segment class.

from line import LineSegment
from carpoint import Point

# Create two points for the line segment.
A = Point(4, 8)
B = Point(3, 9)

# Create a line segment for testing.
line = LineSegment(A, B)

print('Testing endPointA() on line (4,8) (3,9).')
print('Result should be: (4,8)')
print('Result is:       ', line.endPointA(), '\n')

print('Testing endPointB() on line (4,8) (3,9).')
print('Result should be: (3,9)')
print('Result is:       ', line.endPointB(), '\n')

print('Testing length() on line (4,8) (3,9).')
print('Result should be: 1.414')
print('Result is:        %4.3f\n' %(line.length()))

print('Testing slope() on line (4,8) (3,9).')
print('Result should be: -1')
print('Result is:        %d\n' %(line.slope()))

# Create a vertical line segment.
A = Point(4, 2)
B = Point(4, 10)
vLine = LineSegment(A, B)

print('Testing slope() on line (4,2) (4,10).')
print('Result should be: False')
print('Result is:       ', vLine.slope(), '\n')

print('Testing midPoint() on line (4,8) (3,9).')
print('Result should be: (3.5,8.5)')
print('Result is:       ', line.midPoint(), '\n')

print('Testing isVertical() on line (4,2) (4,10).')
print('Result should be: True')
print('Result is:       ', vLine.isVertical(), '\n')

print('Testing isVertical() on line (4,8) (3,9).')
print('Result should be: False')
print('Result is:       ', line.isVertical(), '\n')

# Create a horizontal line segment.
A = Point(3, 10)
B = Point(12, 10)
hLine = LineSegment(A, B)

print('Testing isHorizontal() on line (3,10) (12,10).')
print('Result should be: True')
print('Result is:       ', hLine.isHorizontal(), '\n')

print('Testing isHorizontal() on line (4,8) (3,9).')
print('Result should be: False')
print('Result is:       ', line.isHorizontal(), '\n')

# Create a second vertical line segment.
A = Point(8, 2)
B = Point(8, 10)
vLine2 = LineSegment(A, B)

print('Testing isParallel() on lines (4,2) (4,10) and ((8,2) (8,10).')
print('Result should be: True')
print('Result is:       ', vLine.isParallel(vLine2), '\n')

print('Testing isParallel() on lines (4,8) (3,9) and (4,2) (4,10).')
print('Result should be: False')
print('Result is:       ', line.isParallel(vLine), '\n')

print('Testing isParallel() on lines (4,2) (4,10) and (4,8) (3,9).')
print('Result should be: False')
print('Result is:       ', vLine.isParallel(line), '\n')

A = Point(8, 3)
B = Point(3, 6)
line2 = LineSegment(A, B)

print('Testing isParallel() on lines (4,8) (3,9) and (8,3) (3,6).')
print('Result should be: False')
print('Result is:       ', line.isParallel(line2), '\n')

A = Point(8, 3)
B = Point(7, 4)
line3 = LineSegment(A, B)

print('Testing isParallel() on lines (4,8) (3,9) and (8,3) (7,4).')
print('Result should be: True')
print('Result is:       ', line.isParallel(line3), '\n')



















