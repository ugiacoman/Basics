# CS 141 Lab 10
# line.py
#
# Modified by: Ulises Giacoman

from carpoint import Point

import math

class LineSegment:
    
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        
    def endPointA(self):
        return self.pointA
    
    def endPointB(self):
        return self.pointB
    
    def isVertical(self):
        if self.pointA.xCoord - self.pointB.xCoord == 0:
            return True
        else:
            return False
    
    def isHorizontal(self):
        if self.pointA.yCoord - self.pointB.yCoord == 0:
            return True
        else:
            return False
    
    def length(self):
        return math.sqrt((self.pointA.xCoord - self.pointB.xCoord) ** 2
                         + (self.pointA.yCoord - self.pointB.yCoord) ** 2)
    
    def slope(self):
        if (self.pointA.xCoord - self.pointB.xCoord) == 0:
            return False
        else:
            return (self.pointA.yCoord - self.pointB.yCoord) \
                      / (self.pointA.xCoord - self.pointB.xCoord)
        
    def isParallel(self, otherLine):
        if self.slope() == otherLine.slope():
            return True
        else:
            return False
    
    def midPoint(self):
        midPointX = (self.pointA.xCoord + self.pointB.xCoord) / 2
        midPointY = (self.pointA.yCoord + self.pointB.yCoord) / 2
        return (midPointX, midPointY)