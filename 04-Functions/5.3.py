###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter lastname: ')
age = input_real("Enter age:")
salary = input_real("Enter salary:")
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print("Lastname", last_name)
print("Age:", age)
if is_salary_hidden == False:
    print('Salary', salary)
else:
    print("Salary hidden")
