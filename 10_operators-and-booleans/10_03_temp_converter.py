# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!


currnet_temp = input("What is the current temp in Farenheit? ")

floated_temp = float(currnet_temp)

part_one = (floated_temp - 32)

part_two = part_one * 5//9 

print(part_two)
