#Define a function sum_natural(n) that for the given natural 
# number n calculates the sum of all natural numbers between 1 and n. 
# Apply recursion. 
# Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum_natural(n):
    x = 0 
    for i in range (1,n +1):
        x += i
    return x 

print(sum_natural(10))