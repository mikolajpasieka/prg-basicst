#A text contains any number of words. 
# Define a function f(name) that returns the acronym 
# (first letters of all words). 
# Sample result:
# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"


def f(name):
    words = name.split(' ')
    a = ''
    for i in range(len(words)):
        a += words[i][0]  
    return a


print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))