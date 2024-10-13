#Amount  : 15.84
# VAT 23% :  3.64

amount = float(input("Type an amount:"))
vat = int(input("Type VAT:"))

print(f"The VAT {vat} % from amount: {amount} is {round((amount*vat*0.01),2)}")
