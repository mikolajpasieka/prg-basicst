###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
##
basic_salary = 5000 
total_salary = 0
is_bonus = input("Does the employee receive a bonus(Yes/No)") # does the employee receive a bonus
bonus = 0.15 # 15%

if is_bonus == "Yes":
    total_salary = basic_salary + bonus*basic_salary  
    print(f'Basic salary: {basic_salary}')
    print(f'Bonus included? {is_bonus}')
    print(f'Total salary: {total_salary}')
else:
     print(f'Basic salary: {basic_salary}')
     print(f'Bonus included? {is_bonus}') 


