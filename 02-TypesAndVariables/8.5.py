###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#BPKOPLPW, CHASUS33, DEUTDEFF
swift = input('Enter a SWIFT code: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')