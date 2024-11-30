#Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: the first value of the sequence is 0, 
# the second value is 1. Each subsequent value is the sum of the previous two. 
# Sample result:
# f(5) returns 3
# f(9) returns 21

# Function for nth Fibonacci number
def f(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)

if __name__ == "__main__":
    print(f(5))
    print(f(9))
   