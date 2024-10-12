# a program that calculates the distance to the horizon from a height given in meters from the keyboard
import math
h=input("Enter the height you are at present in meters: ")
d = 3.57*math.sqrt(int(h))
print(f"the distance to the horizon is:{d} km" )