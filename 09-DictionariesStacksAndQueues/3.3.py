import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   stack = queue.LifoQueue()
   error = 0 

   for char in expression:
    if char == "(" or char == "[" or char == "{":
         if stack.get()==char:
            error +=1 
         else:
            stack.put(char)
    elif char == ")":
       if stack.get()!="(":
          error += 1 
    elif char == "}":
       if stack.get()!="{":
          error += 1 
    elif char == "]":
       if stack.get()!="[":
          error += 1 
    
    return error==0#True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
  print("brackets ok")
else:
   print("brackets incorrect")

if brackets_ok(expression2):
   print("brackets ok")
else:
   print("brackets incorrect")

if brackets_ok(expression3):
   print("brackets ok")
else:
   print("brackets incorrect")