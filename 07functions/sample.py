# CS 141 Lab 7
# sample.py
#
# A sample program to demonstrate the use of functions and parameters.
# It extracts two integer values from the user and then divides the 
# two and prints the result.


# The main driver function which should be defined first.

def main():
    # Extract the two input values.
    numerator = int(input("Enter an integer numerator: "))
    denominator = int(input("Enter an integer denominator: ")) 
    print()
    
    # Call the function to perform the division.
    result = divide(numerator, denominator)
    
    # Print the resulting value.
    print("Upon returning to the main function ", end='')
    print(numerator, "divided by", denominator, "equals", result)


# A simple function that divides the value of parameter num by the
# value of parameter den and returns the result.

def divide( num, den ):
    functionResult = num / den
  
    print("In the function, the calculated value of ", end='')
    print(num, "divided by", den, "is", functionResult)
  
    return functionResult
  
  
# Call the main routine in order to run the program.
main()
