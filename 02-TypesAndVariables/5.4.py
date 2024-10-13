import math 

amount = int(input("Type an amount:"))
VAT = int(input("Type VAT:"))
int(amount)
int(VAT)
print(f"The VAT {math.ceil(VAT*100)/100} % from amount: {math.ceil(amount*100)/100} is {math.ceil((amount*VAT*0.01)*100)/100}")
