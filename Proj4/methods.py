file_earthquake = open("earthquake.csv", "r", encoding="windows-1252")
file_earthquake.readline()

country = "NEVADA"

for line in file_earthquake:
    earthquake_info = []
    column = line.split(',')
    
    all_country_list = column[7]
    specific_country_list = []
    
    if  country in all_country_list: 
        all_info_list = [column[0], country]
        specific_country_list.append(all_info_list)
        for line in specific_country_list:
            print("%1s %1s %1s" % line[0], line[1])
       
       
       
       
       
       
       
       
       
       
#print("%1s %1s" %column[1], "/", column[2], "/", column[0], column[7], column[11])