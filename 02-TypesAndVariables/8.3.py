###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.

# determine temperature in degrees Celsius
# convert the given temperature to Kelvin
# convert the given temperature to Fahrenheit

temp_c = int(input('Enter temperature in degree Celcius:'))
temp_k = temp_c + 273.15
temp_f = round((temp_c*33.8),2)

print(f"The temperature in Kelvin is: {temp_k}")
print(f"The temperature in Fahrenheit is: {temp_f}")

