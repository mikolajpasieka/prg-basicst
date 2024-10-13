#a program that reads an integer number from the keyboard 
# and prints that value as a binary and hexadecimal number
#Enter number: 125
#Binary number: 0b1111101
#Hexadecimal number: 0x7d
number = int(input("Enter decimal number:"))
def decimalToBinary(n): 
    return bin(n)

def decimalToHexadecimal(n):
    return hex(n)

if __name__ == '__main__': 
    print(decimalToBinary(number)) 
    print(decimalToHexadecimal(number)) 