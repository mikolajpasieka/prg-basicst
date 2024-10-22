# Write a program that calculates a dog's age in dog's years. 
# For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years. 
# Sample result:
# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

age_h = int(input("Enter the dog's age in human years:"))
if age_h == {1,2}:
    age_d = age_h*10.5
elif age_h > 2:
    age_d = 2*10.5 + (age_h - 2)*4

print(f"The dog's age in dog's years is {age_d} years.")

