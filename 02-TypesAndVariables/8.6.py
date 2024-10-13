###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
import math 
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter in PLN: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))
total_fuel_consumption = math.ceil(distance*fuel_consumption/100*100)/100
total_cost = math.ceil(total_fuel_consumption*fuel_price*100)/100
print(f"Total fuel consumption: {total_fuel_consumption}")
print(f"Total cost: {total_cost} zl")