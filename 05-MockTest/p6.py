sum = 0 
def f(number, even):
    num = str(number)
    if even == True:
        for char in num: 
            if int(char)%2 == 0:
                sum == sum + int(char)
            elif int(num)%2 != 0:
               sum == sum + 0 
    else:
        for char in num: 
            if int(char)%2 != 0:
                sum == sum + int(char)
            elif int(char)%2 == 0:
                sum == sum + 0             
print(sum)
 


if __name__ == "__main__":
    print(f(3124,True))
