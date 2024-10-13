###
# A program that prints your height both in cm and in feet and inches.
#
import math 
cm = 170
feet = int(cm/30.48)
rest = int(cm - (feet*30.48))
inches = math.ceil(rest*0.3937*1)/1
# calculate the number of feet

print('I am ', cm ,'cm tall, i.e. '+str(feet)+' feet and '+str(inches)+ 'inches')