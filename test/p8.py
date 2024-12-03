def f(expression):
    list = expression.split()
    stack = [] # strukturę stosu zaimplementujemy na liście
    for i in list:
        if i == " ":
          continue
        if i.isdigit(): #spawdzam, czy wyrażenie jest liczbą
            n = int(i)
            stack.append(n) # jeśli wczytany element jest liczbą, to wrzuć go na stos
        else:
             b = stack.pop() # jeśli wczytany element jest operatorem, to zdejmij ze stosu dwie liczby a i b
             a = stack.pop()
             if i == '*':
                 stack.append(a*b) # wynik działania wrzuć na stos
             elif i == '-':
                 stack.append(a-b) # wynik działania wrzuć na stos
             elif i == '+':
                 stack.append(a+b) # wynik działania wrzuć na stos
             else:
                 stack.append(a/b) # wynik działania wrzuć na stos
    return stack.pop() # wypisz ostatni i jedyny element znajdujący się na stosie

if __name__ == "__main__": 
    print(f("2 6 + 4 5 - +"))