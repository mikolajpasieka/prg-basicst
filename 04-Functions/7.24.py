# An expression contains operators for adding and subtracting single-digit numbers.
# Define a function f(expression) that returns the value of the expression.
# Sample result:
# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6

def f(expression): 
    x = str(expression)
    for char in x:
        if char == "+":
            y = (int(char[0])) + (int(char[2]))




    return y
 

print(f("2+3"))