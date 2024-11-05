#Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. 
# Sample result:
# f(-7,8) returns 3
# f(-1,11) returns 0


def f(a,b):
    r =0 
    for i in range (a, b):
        if i <0 and i %2 == 0:
            r +=1 
        else: 
            continue
    return r 


print(f(-7,8))
print(f(-1,11))

