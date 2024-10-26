#Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. 
# Write a program that prints a survey consisting of three questions. 
# Save the answers to logical type variables. 
# Then view the survey result. 
##
# Sample result:
##
# SURVEY Are you interested in computer science??  (y/n): y
# Do you like playing computer games? (y/n): n
# Do you have an Instagram account? (y/n): y
##
# SURVEY RESULTS Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes
##

print("SURVEY")
com_sci = input("Are you interested in computer science?? (y/n): ")
games = input("Do you like playing computer games? (y/n):")
inst = input("Do you have an Instagram account? (y/n):")

if com_sci == "y":
    com_sci_b = True
elif com_sci == "n":
    com_sci_b = False
    
if games == "y":
    games_b = True
elif games == "n":
    games_b = False

if inst == "y":
    inst_b = True
elif inst == "n":
    inst_b = False
 
if com_sci_b == True:
    a_1 = "Yes"
else: 
    a_1 = "No" 

if games_b == True:
    a_2 = "Yes"
else: 
    a_2 = "No" 

if inst_b == True:
    a_3 = "Yes"
else: 
    a_3 = "No" 

print("SURVEY RESULTS")
print(f"Interested in computer science: {a_1}")
print(f"Playing computer games: {a_2}")
print(f"Has an Instagram account: {a_3}")