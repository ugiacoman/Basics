# CS 141 lab 11
# testPolygon.py
#
# Modified by:
#
# Test cases for the polygon class

from polygon import Polygon
from carpoint import Point


def main():
    poly = Polygon(Point(0, 0), Point(0, 1), Point(1, 1))
    
    print("Attemptine to print polygon.")
    print("Note: if this doesn't work you have a problem in either \
numVertices or in getVertex\n")
    print("Result should be: { (0,0) (0,1) (1,1) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing insertVertex with (1,0) and 5")
    print("Result should be: False")
    print("Result is:       ",poly.insertVertex(Point(1, 0), 5))
    print("Result should be: { (0,0) (0,1) (1,1) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing insertVertex with (1,0) and -1")
    print("Result should be: False")
    print("Result is:       ",poly.insertVertex(Point(1,0),-1))
    print("Result should be: { (0,0) (0,1) (1,1) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing insertVertex with (2,-1) and 3")
    print("Result should be: True")
    print("Result is:       ",poly.insertVertex(Point(2, -1), 3))
    print("Result should be: { (2,-1) (0,0) (0,1) (1,1) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing insertVertex with (1,0) and 3")
    print("Result should be: True")
    print("Result is:       ",poly.insertVertex(Point(1, 0), 3))
    print("Printing resulting polygon:")
    print("Result should be: { (2,-1) (0,0) (0,1) (1,1) (1,0) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing findVertex with (1,1)")
    print("Result should be: 3")
    print("Result is:        ",poly.findVertex(Point(1, 1)),"\n")
    
    print("Testing findVertex with (1,2)")
    print("Result should be: False")
    print("Result is:       ",poly.findVertex(Point(1, 2)),"\n")
    
    print("Testing getVertex with -1")
    print("Result should be: False")
    print("Result is:       ",poly.getVertex(-1),"\n")
    
    print("Testing getVertex with 5")
    print("Result should be: False")
    print("Result is:       ",poly.getVertex(5),"\n")
    
    print("Testing deleteVertex with -1")
    print("Result should be: False")
    print("Result is:       ",poly.deleteVertex(-1))
    print("Result should be: { (2,-1) (0,0) (0,1) (1,1) (1,0) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing deleteVertex with 6")
    print("Result should be: False")
    print("Result is:       ",poly.deleteVertex(6))
    print("Result should be: { (2,-1) (0,0) (0,1) (1,1) (1,0) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing deleteVertex with 0")
    print("Result should be: True")
    print("Result is:       ",poly.deleteVertex(0))
    print("Printing resulting polygon:")
    print("Result should be: { (0,0) (0,1) (1,1) (1,0) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")
    
    print("Testing perimeter")
    print("Result should be: 4.0")
    print("Result is:       ",poly.perimeter(),"\n")
    
    print("Testing deleteVertex with 2 and then 1 ")
    print("Result should be: True")
    print("Result is:       ",poly.deleteVertex(2))
    print("Printing resulting polygon:")
    print("Result should be: { (0,0) (0,1) (1,0) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("Result should be: False")
    print("Result is:       ",poly.deleteVertex(1))
    print("Printing resulting polygon:")
    print("Result should be: { (0,0) (0,1) (1,0) }")
    print("Result is:        ", end="")
    printPoly(poly)
    print("")

def printPoly(poly):
    print("{ ", end="")
    for i in range(poly.numVertices()):
        print(poly.getVertex(i), " ",sep="", end="")
        
    print("}")
    
    
main()




































