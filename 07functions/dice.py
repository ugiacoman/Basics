# CS141 - Lab 7
# dice.py
#
# Modified by: Ulises Giacoman
#
# 
# 

import random

# The main driver routine. 

def main():
    print("Simulate the rolling of a die.\n")
    action = input("Press <ENTER> to roll the die or enter <q> to quit: ")
    while action != 'q' :
        faceOfDie = rollDie()
        faceOfDieTwo = rollDie()
        print("You rolled a", faceOfDie, "and a", faceOfDieTwo)
        print( buildDie(faceOfDie) )
        print("")
        print(buildDie(faceOfDieTwo))
        
        action = input("Press <ENTER> to roll the die or enter <q> to quit: ")
    
  
# Simulates the rolling of a 6-sided die using the random number 
# generator. The face value is returned.

def rollDie() :
    FaceofDie = random.randint(1,6)
    
    return FaceofDie
    
    
    
  
# Builds and returns a text-based version of the die face as a string 
# based on the face value passed as a argument.

def buildDie( faceValue ) :
    if faceValue == 1:
        faceofDie = " -----\n|     |\n|  *  |\n|     |\n -----"
    elif faceValue == 2:
        faceofDie = " -----\n|*    |\n|     |\n|    *|\n -----"
    elif faceValue == 3:
        faceofDie = " -----\n|*    |\n|  *  |\n|    *|\n -----"
    elif faceValue == 4:
        faceofDie = " -----\n|*   *|\n|     |\n|*   *|\n -----"
    elif faceValue == 5:
        faceofDie = " -----\n|*   *|\n|  *  |\n|*   *|\n -----"
    elif faceValue == 6:
        faceofDie = " -----\n|*   *|\n|*   *|\n|*   *|\n -----"
        
    return faceofDie
        
       
    
  
    
# Call the main routine.  
main()  