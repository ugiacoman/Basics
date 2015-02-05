# CS 141 Project 3
# Proj4.py
# Modified by both: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                   Bradley Blount (202)-380-6688 beblount@email.wm.edu
#
# Analyzing large amounts of data is something that modern man does all
# the time. This data is often in spreadsheet form which can easily be  
# converted to comma-separated-value format.
#
# This project is a menu driven project which allows the user to pull 
# different kinds of information from the earthquake.csv file by 
# putting it in list form making it easier to analyze.

def createTopTwentyList(columnNumber):
      ''' Creates top twenty list for column in earthquake.csv '''
      generalList = []
      for line in eqFile:
            column = line.split(',')
            line = column[columnNumber]
            
            if line != '':
                  allInfoList = [float(line), column[7], column[0]]
                  generalList.append(allInfoList)
                  
      generalList.sort(reverse = True)
      topTwenty = generalList[0:20]     
      
      return topTwenty      


def createLocationList(location):
      ''' Creates list of a country's or state's history of earthquakes '''
      specificLocationList = []
      for line in eqFile:
            column = line.split(',')
            allLocationList = column[7]           
            # Creates lists out of csv file information 
            if location in allLocationList: 
                  allInfoList = [column[1], column[2], column[0],
                                   column[7], column[11]]
                  specificLocationList.append(allInfoList)
                  
      return specificLocationList


def createSummationList(columnNumber):
      ''' Creates list that add all numbers for a column in earthquake.csv '''
      numbersList = []
      total = 0
      for line in eqFile:
            column = line.split(',')
            # Sums the numbers in the lists
            if column[columnNumber] != '': 
                  column = float(column[columnNumber])
                  numbersList.append(column)
            
      total = sum(numbersList)

      return total                  
      


def topTwenty():
      ''' Prompts user to choose the top twenty of a statistic '''
      print('Which top 20 do you want: ')
      print('a) magnitude')
      print('b) number of deaths')
      print('c) number of injuries')
      print('d) amount of damage')
      print('e) number of houses destroyed')
      print('f) number of houses damaged')
      print()
      optionWhichTwenty = input('Enter choice: ').lower()
      print(optionWhichTwenty)
      print()    
      
      # Uses user's input to create the top twenty list specified and prints 
      if optionWhichTwenty == 'a':
            topTwentyMagnitudeList = createTopTwentyList(11)
            print('Top 20 earthquakes by magnitude')
            print()
            
            for line in topTwentyMagnitudeList:
                  print('%-7s %-45s %1s' % (line[2], line[1],
                                            float(line[0]))) 
                  
      elif optionWhichTwenty == 'b':
            
            topTwentyDeathsList = createTopTwentyList(13)
            print('Top 20 earthquakes by number of deaths')
            print()            
            
            for line in topTwentyDeathsList:
                  print('%-7s %-53s %7s' % (line[2], line[1],
                                            '{:,d}'.format(int(line[0]))))
                  
      elif optionWhichTwenty == 'c':
            
            topTwentyInjuriesList = createTopTwentyList(15)
            print('Top 20 earthquakes by number of injuries')
            print()            
            
            for line in topTwentyInjuriesList:
                  print('%-7s %-53s %7s' % (line[2], line[1], 
                                            '{:,d}'.format(int(line[0])))) 
                  
      elif optionWhichTwenty == 'd':
            
            topTwentyDamagesList = createTopTwentyList(17)
            print('Top 20 earthquakes by amount of damage')
            print()            
            
            for line in topTwentyDamagesList:
                  print('%-7s %-53s %s%15s' % (line[2], line[1], \
                              '$', '{:,d}'.format(int(line[0]*1000000))))
                  
      elif optionWhichTwenty == 'e':
            
            topTwentyHousesDestroyedList = createTopTwentyList(19)
            print('Top 20 earthquakes by number of houses destroyed')
            print()            
            
            for line in topTwentyHousesDestroyedList:
                  print('%-7s %-53s %9s' % (line[2], line[1], 
                                            '{:,d}'.format(int(line[0]))))
                  
      elif optionWhichTwenty == 'f':
            
            topTwentyHousesDamagedList = createTopTwentyList(21)
            print('Top 20 earthquakes by number of houses damaged')
            print()            
            
            for line in topTwentyHousesDamagedList:
                  print('%-7s %-53s %9s' % (line[2], line[1], 
                                           '{:,d}'.format(int(line[0])))) 
                  
      else:
            print("You've entered an incorrect option.")
                  
      
   
def quakesInLocation():
      ''' Prompts user for location to display its earthquakes instances '''
      print('Print out all quakes from a certain country or state')
      location = input('Enter country name or state: ').upper()
      print(location)
      print()
      
      specificLocationList = createLocationList(location)
      count = 0 # Accounts for a location w/ 0 quakes 
      for line in specificLocationList:     
            date = line[0] + '/' + line[1] + '/' + line[2]
            print('%-12s %-50s %10s' % (date, line[3], line[4]))
            count += 1
      
      if count <= 0:
            print(location, 'has had no earthquakes')
            
                                

def summation():
      ''' Produces a summation of a chosen statistic '''
      print('Which summation do you want: ')
      print('a) total number of deaths')
      print('b) total number of injuries')
      print('c) total amount of damage')
      print('d) total number of houses destroyed')
      print('e) total number of houses damaged')
      print()
      optionSummation = input('Enter choice: ')
      print()
      
      if optionSummation == 'a':
            total = int(createSummationList(13))
            print('The total number of deaths recorded:',
                  '{:,d}'.format(total))     
            
      elif optionSummation == 'b':
            total = int(createSummationList(15))
            print('The total number of injuries recorded:',
                  '{:,d}'.format(total))
            
      elif optionSummation == 'c':
            total = createSummationList(17)
            print('The total amount of damage recorded:', '$'
                  '{:,.2f}'.format(total*1000000))       
            
      elif optionSummation == 'd':
            total = int(createSummationList(19))
            print('The total number of houses destroyed:',
                  '{:,d}'.format(total)) 
            
      elif optionSummation == 'e':
            total = int(createSummationList(15))
            print('The total number of houses damaged:',
                  '{:,d}'.format(total))           
     
      else:
            print("You've entered an incorrect option.")            


            
choice = ''
while choice != 'q':  # Allows for game to contuniue running 
      ''' Main Loop '''
      eqFile= open('earthquake.csv', 'r')
      eqFile.readline()
      
      if choice == 'a':
            topTwenty()       
      elif choice == 'b':
            quakesInLocation()
      elif choice == 'c':
            summation()
      else:
            print("You've entered an incorrect option. Try again")

      print()
      print('Menu Options')
      print('a) Print top 20 quakes based on a given criteria')
      print('b) Print quakes in a certain country or state')
      print('c) Summation information')
      print('q) Quit')
      print()
      choice = input('Enter choice: ').lower()
      print(choice)
      print()
      
      
print('Thank you')
eqFile.close()