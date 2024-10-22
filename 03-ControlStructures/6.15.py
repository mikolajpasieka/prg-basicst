#EAN-13 (European Article Number) is a barcode for marking goods.
#The first 3 digits (590) usually indicate goods manufactured in Poland.
# Write a program that checks whether the EAN-13 number entered 
# from the keyboard consists of exactly 13 characters (digits). 
# Print a message if the number is correct. 
# Additionally, only when the article number is correct, 
# print a message when the product was manufactured in Poland. 
# Sample result:
# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland

number = input("Enter EAN-13 article number:")
number_len = len(number)
if number_len == 13:
    dig = "corrtect"
else:
    dig = "incorrect"
print(f"Article number is {dig}")
if number[0:3] == "590":
    print("Article manufactured in Poland")
