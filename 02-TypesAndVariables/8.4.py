###
# A program that prints your height both in cm and in feet and inches.
# 
cm = 170
feet = float(cm/30.48)
rest = float(cm - (feet*30.48))
inches = round((rest*0.3937), 0 )
# calculate the number of feet

print('I am ', cm ,'cm tall, i.e. '+str(feet)+' feet and '+str(inches)+ 'inches')