# CS 141 Lab 3
# banking.py 
#
# Modified by: Ulises Giacoman
#
# This program prompts the user for whether he/she will be withdrawing or
# deposting money. Then the program prompts for the amount. Only valid actions
# are allowed. The user may not overwithdraw, nor input negative value. 


Balance = 2010

print("Welcome to the CS141 Bank")
depOrWithChoice = (input("Please choose either (D)eposit  (W)ithdrawal "))         
print(depOrWithChoice)

# Calculate withdrawl and deposit. Exits out with invalid input.
if depOrWithChoice.lower() == "w":
    depOrWithAmount = float(input("Please enter amount "))
    print(depOrWithAmount)
    Balance = Balance - depOrWithAmount
    if depOrWithAmount < 0:
        print("Amount must be >= 0.0")
    elif Balance < 0:
        print("You can not overdraw your account!!")
    else:
        print("You now have $", Balance)    
        
elif depOrWithChoice.lower() == "d":
    depOrWithAmount = float(input("Please enter amount "))
    print(depOrWithAmount)
    Balance = Balance + depOrWithAmount
    if depOrWithAmount < 0:
            print("Amount must be >= 0.0")
    elif Balance < 0:
        print("You can not overdraw your account!!") 
    else:
        print("You now have $", Balance)   
            
else:
    print("Invalid Option.")

