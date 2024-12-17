employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e: employees[0]=="J", employees))
# print a list …
print(emp_J)