###
# A program that prints your height both in cm and in feet and inches.
# 
import math
cm = 170
feet = math.floor(float(cm) / 2.54 / 12)
inches = round((float(cm) / 2.54 / 12 - feet) * 12)
# calculate the number of feet
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
