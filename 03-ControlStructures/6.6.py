#The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:
# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

time = int(input("enter the number of hours of parking:"))
if time >= 1 and time <= 2:
    fee = time*5
if time >= 3 and time <= 6:
    fee = 10 + (time-2)*15
if time >6:
    fee = 70 + (time-6)*20

print("the fee is", fee)