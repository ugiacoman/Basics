# CS141 lab 6
# mathtable.py
#
# Modified by: Ulises Giacoman
#
# A program that produces a table containing the squares,
# square roots, and log values for a sequence of numbers.

import math

BEGIN = 1.0   # starting value for x
END = 10.0    # ending value for x
INC = 0.5     # amount to increment x by
   
# Writes file and opens  
file = open('table.txt', 'w')
      
# Writes the table header in table.txt      
file.write( "Mathematical Table\n" )
file.write( "     x  |          x^2      sqrt(x)       log(x)\n" )
file.write( "-" * 50)
file.write("\n")
                          
# Writes the table of values into table.txt. 
x = BEGIN
while x <= END :
    xSqr = x * x
    xSqrt = math.sqrt(x)
    xLog = math.log(x)
  
    file.write( "%7.2f | %12.2f %12.2f %12.2f\n" % (x, xSqr, xSqrt, xLog) )
    x += INC

file.write( "-" * 55 )
file.close()