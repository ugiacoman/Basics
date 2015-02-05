file_earthquake = open("earthquake.csv", "r", encoding="windows-1252")
file_earthquake.readline()



def create_country_list(country):  # make an option parameter?
      ''' Creates top twenty list for column in earthquake.csv '''
      general_list = []
      for line in file_earthquake:
          
            column = line.split(',')
            line = column[country]
            
            if line == country:
                  country_list = [column[7]]
                  print(country_list)
                 
      return country_list 

country = input("enter country: ")
country_list = create_country_list(country)

for line in country_list:
        print("%-7s %-53s %1s" % (line[2], line[1], line[0])) 