# CS 141 Project 2
# Proj2.py 
#
# Modified by both: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                   Bradley Blount  (202)-380-6688 beblount@email.wm.edu
#
# This program prompts the user for a date. With this information
# it calculates the Western and Chinese Zodiac signs and prints them. After,
# it prompts the user to see if the user wants to do it again. If yes, then
# it will repeat the process. If no, it will exit.

count = 0
invalid = 0
check1 = 0
check2 = 0
check3 = 0

#Decides whether to calculate the Zodiac sign or not
while count == 0 or choice_str == "y":
    
    if invalid > 0:
        date = input("Please enter a valid date: ")
    else:
        date = input("Please enter a date in the form mm dd yyyy: ")
    
    month, day, year = date.split(" ")
    print(month, day, year) 
    print()
    month = int(month)
    day = int(day)
    year = int(year) 

# Checks whether it is a leap year
    if month in range(3, 13) and day in range(1, 32) \
        and year in range(1901, 2100):
            check1 = 1
    elif month == 2 and year % 4 == 0 and day in range(1,30):
            check2 = 1
    elif month == 2 and year % 4 != 0 and day in range(1,29):
            check3 = 1

    if check1 == 1 or check2 == 1 or check3 == 1:

#Calculates Western Zodiac sign
        if month == 12:
            if day in range(22, 32):
                western_sign = "Capricorn"
            else:
                western_sign = "Sagittarius"
        elif month == 1:
            if day in range(20, 32):
                western_sign = "Aquarius"
            else: 
                western_sign = "Capricorn"
        elif month == 2:                   
            if day in range(19, 30):
                western_sign = "Pisces"
            else: 
                western_sign = "Aquarius"        
        elif month == 3:
            if day in range(21, 32):
                western_sign = "Aries"
            else: 
                western_sign = "Pisces"         
        elif month == 4:
            if day in range(20, 32):
                western_sign = "Taurus"
            else:
                western_sign = "Aries"
        elif month == 5:
            if day in range(21, 32):
                western_sign = "Gemini"
            else:
                western_sign = "Taurus"
        elif month == 6:
            if day in range(22, 32):
                western_sign = "Cancer"
            else:
                western_sign = "Gemini"
        elif month == 7:
            if day in range(23, 32):
                western_sign = "Leo"
            else:
                western_sign = "Cancer"
        elif month == 8:
            if day in range(23, 32):
                western_sign = "Virgo"
            else:
                western_sign = "Leo"
        elif month == 9:
            if day in range(23, 32):
                western_sign = "Libra"
            else:
                western_sign = "Virgo"
        elif month == 10:
            if day in range(24, 32):
                western_sign = "Scorpio"
            else:
                western_sign = " Libra"
        elif month == 11:
            if day in range(22, 32):
                western_sign = "Sagittarius"
            else:
                western_sign = "Scorpio"

# Calculates Chinese Zodiac sign
        if year in range(1901, 2100, 12):
            chinese_sign = "Ox."
        elif year in range(1902, 2100, 12):
            chinese_sign = "Tiger."
        elif year in range(1903, 2100, 12):
            chinese_sign = "Rabbit."
        elif year in range(1904, 2100, 12):
            chinese_sign = "Dragon."
        elif year in range(1905, 2100, 12):
            chinese_sign = "Snake."
        elif year in range(1906, 2100, 12):
            chinese_sign = "Horse."
        elif year in range(1907, 2100, 12):
            chinese_sign = "Sheep."
        elif year in range(1908, 2100, 12):
            chinese_sign = "Monkey."
        elif year in range(1909, 2100, 12):
            chinese_sign = "Rooster."
        elif year in range(1910, 2100, 12):
            chinese_sign = "Dog."
        elif year in range(1911, 2100, 12):
            chinese_sign = "Pig."
        elif year in range(1912, 2100, 12):
            chinese_sign = "Rat."

# Prints the user's signs
        print("Your signs are", western_sign, "and the", chinese_sign)
        print("******************************************")
        print()
        choice_str = input("Would you like to do another? ")
        print(choice_str)
        choice_str = choice_str.lower()
        print()
        count = count + 1 
        invalid = 0
        check1 = 0
        check2 = 0
        check3 = 0
        if choice_str == "n":
            print()
            
    elif check1 != 1 or check2 != 1 or check3 != 1: 
        print("Sorry, this is not a valid date.")
        invalid += 1