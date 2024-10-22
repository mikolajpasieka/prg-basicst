# In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products and the product price from the keyboard. 
# 
# Sample result:
# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

number = int(input("Number of products purchased:"))
price = int(input("Product price:"))
if number% 2 ==0:
    amount = price + 0.75*price*(number-1)
if number% 2 !=0:
    amount = (number%2 + 1)*price + price*0.75*(number - (number%2 + 1))
    
print(f"Amount to pay:{amount}")