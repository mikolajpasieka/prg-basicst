###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    i = 1 
    for line in file:
        print(i,".",line, end="", sep="")
        i += 1 
        