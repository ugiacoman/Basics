# CS 141 Project 3
# Proj3.py 
#
# Modified by both: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                   Bradley Blount  (202)-380-6688 beblount@email.wm.edu
#Prologue:

# For the first game the objective is to find all the words of a particular
# length containing just a single vowel that does not have a particular letter
# in it. In the procedure for this game, the program will ask for the length of
# the words you are looking for and a letter that will be missing from each 
# word and then find and print the words that match this criteria that have only
# a single vowel (defined as a,e,i,o and u).
#
# In the second game the objective is to find all the words containing all the 
# letters of a particular word (in no particular order). In the procdure for 
# this game, the user will enter the word whose letters he/she is looking for.
# For example, if the user enters memphis, the program should return mimeographs
# as one of the words that contains all the letters of memphis. In addition, the
# user will enter a maximum length of the words they want to see. The procedure 
# will find and print the words that contain all the letters of the given word.
# 
# In the third game the objective is find all the words that contain a particular
# string.
#
# In the fourth program the objective is to The program will ask for the string
#the user is looking for which is then entered from keyboard. All words 
#containingthis string are then printed. The program should ask for a word
#length and the program should find all words that have this same propert
#for that word length.

file_dict = open("dictionary.txt", "r")


# Game A
def game_a():
      '''Procedure for game A. Gets input for word length and excluded letter'''
      length_of_word = int(input("Please enter the word length you are \
looking for: "))
      print(length_of_word)   
      
      letter_excluded = input("Please enter the letter you'd like to \
exclude: ").lower()
      print(letter_excluded)
      print('')
      
      '''Accounts for no word match'''
      match = False
      for word in file_dict:
         word = word.strip()
         count = 0
         vowels = "aeiou"
         for char in word:
            if char in vowels:
               count += 1
         if len(word) == length_of_word and letter_excluded not in word \
and count == 1:
            print(word)
            match = True
            
      if not match:
         print("There are no words that fit this criteria.") 
                  
            
# Game B
def game_b():
      '''Prompts user for string and maximum length of words to look for.'''
      include = input("Enter word: " )
      print(include)
      length = int(input("What is the maximum length of the words \
you want: "))   
      print(length)
      print('')
      
      '''Accounts for no word match'''
      match = False
      for word in file_dict:
          word = word.strip()
          x = word
          if len(word) <= length:
              count = 0
              for letter in include:
                  if letter in word:
                      count += 1
                      word = word.replace(letter, "", 1)
              if count == len(include):  
                  print(x)
                  match = True
            
      if not match:
               print("There are no words that fit this criteria.")             
   
                  
# Game C
def game_c():
      '''Prompts user for exact string to look for'''
      word_exact= input("Enter the exact string you are looking for: ")
      print(word_exact)
      print('')
      
      '''Accounts for no word match'''
      match = False
      for word in file_dict:
         word = word.strip()
         if word_exact in word:
            print(word)
            match = True
      if not match:
         print("There are no words that fit this criteria.")              


# Game D
def game_d():
      '''Prompts user for length of word with overlapping letters'''
      file_dict.seek(0)
      wordLength = int(input("Enter the length of the words " \
                             "you are looking for: "))
      print(wordLength)
      states = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI',\
              'ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN',\
              'MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH',\
              'OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA',\
              'WV','WI','WY']        
     
      '''Accounts for no word match''' 
      match = False
      for word in file_dict:
          word = word.strip().upper()
          if len(word) == wordLength:
              wordChoice = 0
              for i in range (wordLength-1) :
                  if word[i : i + 2] in states:
                      wordChoice +=1
              if wordChoice == len(word)-1:
                  print('')  
                  print(word)
                  match = True  
                  
      if not match:
            print('')
            print("There are no words that fit this criteria.")                    


# Opening prompt
print('')
print("Let's play a game")
print('')
print("Choose which game you want to play")
print("a) Find words with only one vowel and excluding a specfic letter.")
print("b) Find words containing all the letters of another word with a \
maximum length")
print("c) Find words containing a particular string")
print("d) Find words containing overlapping state abbreviations")
print("q) Quit")

print('')
choice = input("Enter choice: ").lower()
print(choice)
print('')

# Main Loop
while choice != "q":
      if choice == "a":
            game_a()       
      elif choice == "b":
            game_b()
      elif choice == "c":
            game_c()
      elif choice == "d":
            game_d()
      else:
            print("You've entered an incorrect choice. Try again")
      
      file_dict.seek(0) # Keeps file open 
      print("")
      print("Choose which game you want to play")
      print("a) Find words with only one vowel and excluding a specfic \
letter.")
      print("b) Find words containing all the letters of another word with \
a maximum length")
      print("c) Find words containing a particular string")
      print("d) Find words containing overlapping state abbreviations")
      print("q) Quit")
      print('')
      choice = input("Enter choice: ").lower()
      print(choice)
      print('')
print("Thanks for Playing")
file_dict.close()
