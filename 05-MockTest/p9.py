sum = 0 
def f(sentence):
    sen = str(sentence)
    for char in sen:
        if char == 'a' or char == "e" or char == 'i' or char == 'o' or char == 'u' or char == 'y': 
            sum =+ 1   
        else:
            continue
print(sum)
    


if __name__ == "__main__":
    print(f("water"))
    