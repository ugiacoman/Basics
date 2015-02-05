

def create_top_twenty_earthquakse_list(file_earthquake):
    """Create a list of cars and mileage from file_earthquake"""
    # 2a create a mileage list and initialize it to empty
    earthquakes_list = []

    for line in file_earthquake:
        if line[0:5] == 'YEar' or 'VAN' in line or 'PICKUP' in line: #this wrong
            line_list = line.split(',')    
            earthquakes_tuple = (int(line_list[0]), line_list[7], line_list[11]) #this wrong
            earthquakes_list.append(earthquakes_tuple)
    return earthquakes_list


# 1. open Earthquake data file
file_earthquake = open("earthquake.csv", "r")
earthquakes_list = create_top_twenty_earthquakse_list(file_earthquake)

# 3. find max and min mileage
max_mileage = max(earthquakes_list)
min_mileage = min(earthquakes_list)

print("Max and Min Mileage: ", max_mileage, min_mileage)