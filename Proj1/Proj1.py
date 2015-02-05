#Proj1.py

# Modified by Ulises Giacoman and Bradley Blount

# First the program asks for the input, as a float, of the amount of gallons
# of gasoline. Then the program converts the gallons of gasoline to: liters
# gallons per barrel, CO2 output, British Thermal Units, ethanol gallons,
# and the cost at $3.20 per gallon. After the conversions, the program
# prepares for displaying the output by creating strings. Lastly, the program
# displays the output.


# Prompt for gallons of gasoline
gallons = float(input("Gallons of gasoline: "))
print(gallons)

# Converts gallons of gasoline
liters_fl = gallons * 3.78541178
barrels_fl = gallons / 19.5
co2_fl = gallons * 20
bTU_fl  = gallons * 115000
ethanol_fl = bTU_fl / 75700
cost_fl = gallons * 3.20

# Defining strings for display
liters_str = "The number of liters is:"
barrels_str = "The number of barrels of oil is:"
co2_str = "The pounds of CO2 produced is:"
bTU_str = "The number of BTUs produced is:"
ethanol_str = "The number of gallons of ethanol "
ethanol_str2 = "for the same BTUs is:"
cost_str = "The cost of the gasoline at $3.20 "
cost_str2 = "would be:"

# Display results of conversions
print("--------------------------------------------------------------------")
print()
print("For %1.2f gallons of gasoline, the following conversions apply:" % \
(gallons))
print()
print("%36s %12.2f" % (liters_str, liters_fl))
print("%36s %12.2f" % (barrels_str, barrels_fl))
print("%36s %12.2f" % (co2_str, co2_fl))
print("%36s %12.2f" % (bTU_str, bTU_fl))
print("%36s" % (ethanol_str))
print("%36s %12.2f" % (ethanol_str2, ethanol_fl))
print("%36s" % (cost_str))
print("%36s $ %10.2f" % (cost_str2, cost_fl))
print()
print("--------------------------------------------------------------------")