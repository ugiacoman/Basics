# CS141 - Lab 7
# meters.py
#
# Modified by: Ulises Giacoman
#
# Extracts a measurement given in feet and inches from the user, 
# then converts the measurement to meters and displays the result.  


# The main driver function.
def main():
    print("Enter a measurement.")
    feet = float(input("Enter the feet: "))
    inches = float(input("Enter the inches: "))
    meters = convertToMeters(feet, inches)
    
    print(feet, "feet and", inches, "inches is", meters, "meters")
  
  
# Converts the given measurement (feet and inches) to meters. The
# meters measurement is returned as a floating-point value.
def convertToMeters( feet, inches ):
    feetToInches = feet * 12
    meters = (feetToInches + inches) / 39.37
    
    return meters

# Call the main routine.  
main()  
