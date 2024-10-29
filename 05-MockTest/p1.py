

def f(amount_to_pay):
    n_5 = round(amount_to_pay/5, 2)
    n_2 = round((amount_to_pay%5)/2, 2) 
    n_1 = amount_to_pay - (n_5*5 + n_2*2)
    coins = n_1 + n_2 + n_5
    print(coins)
    
       
if __name__ == "__main__":
    print(f(23))
    print(f(8))