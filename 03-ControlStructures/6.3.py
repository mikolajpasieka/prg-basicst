###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = bool(input("Is switch off (Enter False) or on (Enter True):")) # False - switch off, True - switch on
light_switch2 = bool(input("Is switch off (Enter False) or on (Enter True):"))
bulbs_on = 0
if light_switch1 == True:
    bulbs_on += 1
elif light_switch2 == True:
    bulbs_on += 2 
elif light_switch1 == True and light_switch2 == True:
    bulbs_on += 3
else: 
    bulbs_on = 0 

print(f"{bulbs_on} bulbs are illuminating the house ")