#The sequence of digits contains the number of points rolled with a dice. 
# Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice):
    dice1 = str(dice)
    a = int(dice1.count("1"))
    b = int(dice1.count("2"))
    c = int(dice1.count("3"))
    d = int(dice1.count("4"))
    e = int(dice1.count("5"))
    f = int(dice1.count("6"))
    if a > b and a > c and a > d and a > e and a >f: 
        x = 1
    elif b > a and b > c and b > d and b > e and b > f:
        x = 2
    elif c > a and c > b and c > d and c > e and c > f:
        x = 3
    elif d > a and d > b and d > c and d > e and d > f:
        x = 4
    elif e > a and e > b and e > c and e > d and e > f: 
        x = 5
    elif f > a and f > b and f > c and f > d and f > e: 
        x = 6 
    return x 

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))

