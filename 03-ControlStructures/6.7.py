#Write a program that asks the user for their age and then checks which age group they belong to:
#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older

age = int(input("enter your age:"))
if age < 13:
    print("You are a child")
elif age >=13 and age <= 19:
    print("You are a teen")
elif age >= 20 and age <= 64:
    print("You are an adult")
else:
    print("You are a senior")