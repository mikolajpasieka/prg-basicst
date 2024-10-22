#Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard.
####
# Sample result:
#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

time = input("enter time (24-hour format):")
if int(time[0:2]) <= 12:
    print(f"Time in 12-hour format: {time}am")
else:
    h = int(time[0:2])-12
    min = time[3:5]
    print(f"Time in 12-hour format:{h}:{min}pm")