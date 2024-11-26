#Write a program that converts any natural number to a binary number. 
# Use the stack. 
# To convert a number, divide the number by 2, 
# each time taking the remainder of the division 
# and putting the remainder on the stack. 
# Repeat the division until the number
#  you are dividing is zero. 
# Then pop and display all values from the stack. 
#Sample result for number 18:
import queue
def f(n):
    bin = queue.LifoQueue()
    bin_num = ""
    while  n/2 != 0:
        bin.put(n%2)
        n = n/2 - n%2
    while not bin.empty():
        bin_num = bin.get()
    
    return bin_num
if __name__ == "__main__":
    print(f(18))
