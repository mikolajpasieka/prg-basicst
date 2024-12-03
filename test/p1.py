def f(player1, player2):
    total1 = 0
    total2 = 0 
    if "A" or "K" or "Q" or "J" or "T" in player1:
        total1 += 10
    if "K" in player1:
        total1 += 10
    if "Q" in player1:
        total1 += 10
    if "J" in player1:
        total1 += 10
    if "T" in player1:
        total1 += 10
    if "9" in player1:
        total1 += 9
    if "8" in player1:
        total1 += 8
    if "7" in player1:
        total1 += 7
    if "6" in player1:
        total1 += 6
    if "5" in player1:
        total1 += 5
    if "4" in player1:
        total1 += 4
    if "3" in player1:
        total1 += 3
    if "2" in player1:
        total1 +=2 

    if "A" in player2:
        total2 += 10
    if "K" in player2:
        total2 += 10
    if "Q" in player2:
        total2 += 10
    if "J" in player2:
        total2 += 10
    if "T" in player2:
        total2 += 10
    if "9" in player2:
        total2 += 9
    if "8" in player2:
        total2 += 8
    if "7" in player2:
        total2 += 7
    if "6" in player2:
        total2 += 6
    if "5" in player2:
        total2 += 5
    if "4" in player2:
        total2 += 4
    if "3" in player2:
        total2 += 3
    if "2" in player2:
        total2 +=2 

    if total1 >= total2:
        x = True
    else: 
        x = False
    return x 


if __name__ == "__main__": 
    print( f("AJ972","AQT72") ) 
    print( f("9532","K8") ) 
    