#The data below contains a price list of items from a 
# clothing store along with their prices. Due to a seasonal sale, 
# the store is reducing the price of each item by 10%. 
# Write a program that:
# prints a list of products and their prices before the discount
# prints the total value of the products before the discount
# modifies the price list according to the discount (round prices to two decimal places)
# prints a list of products and their prices after the 10% discount
# prints the total value of the products after the discount


price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key,value in price_list.items():
   print(f"{key} : {value}")

total = 0
for key,value in price_list.items():
   total += value

print(round(total,2))

for key,value in price_list.items():
   vaule = round((0.90*value), 2)

for key,value in price_list.items():
   print(f"{key} : {value}")

total1 = 0
for key,value in price_list.items():
   total1 += value

print(round(total1,2))