###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#

distance = float(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter in PLN: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))
total_fuel_consumption = round((distance*fuel_consumption/100), 2)
total_cost = round((total_fuel_consumption*fuel_price),2)
print(f"Total fuel consumption: {total_fuel_consumption}")
print(f"Total cost: {total_cost} zl")