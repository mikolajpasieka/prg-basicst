#A palindrome is an expression that sounds the same when read backwards. Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. Sample result:
# f("radar") returns True
# f("12-11-21") returns True
# f("book") returns False

def f(palindrome):
    x = str(palindrome)
    y = ""
    for char in x:
        y = char + y   
    if (x == y):
        p = True
    else:
        p = False
    return p 

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))

