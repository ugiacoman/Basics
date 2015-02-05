# CS 141 lab 11
# fraction.py
#
# Modified by:
#
# A class that represents a fraction or rational number.

import math
import sys

class Fraction:
    def __init__(self, num, den):
       # The denominator can not be zero. If it is, abort the program.
        if den == 0: 
            sys.exit("Divide by zero")
        
       # Compute the greatest common divisor and reduce the numerator
       # and the denominator.
        div = gcd(num, den)
        self.num = abs(num // div)
        self.den = abs(den // div)
      
       # A negative fraction will be indicated by a negative numerator. 
        if num * den < 0: 
            self.num = -self.num
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den) 
      

# greatest common divisor function
# param:
# bigger  int   one of the two numbers which is bigger than the other
# smaller int   one of the two numbers which is smaller than the other
#
# return: the greatest common divisor of bigger and smaller
def gcd(bigger, smaller):
    while smaller != 0:
        temp = smaller
        smaller = bigger % smaller
        bigger = temp
    return bigger


