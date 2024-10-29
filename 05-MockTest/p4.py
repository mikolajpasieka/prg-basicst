def f(card_number):
    number = str(card_number)
    print(f"{number[0:2]}**********{number[12:16]}")
    

if __name__ == "__main__":
    print(f(5290312400019022))
    