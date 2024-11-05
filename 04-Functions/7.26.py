# Define a function f(text) that returns the 
# given text with all characters separated by a dash sign. 
# Example:
# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""

def f(text): 
    c = " "
    c1 = " "
    x = str(text)
    z = int(len(x))
    for char in x: 
     if char == x[0:z-2]:
          for char  in x :
           c = c + char + "-" 
     elif char == x[z-1]:
        for char in x: 
           c1 = c1 + char
    y = c + c1 
        
    return y 

if __name__ == "__main__":
    print(f("Univesity"))
    print(f("UE"))
    print(f("x"))
    print(f(""))