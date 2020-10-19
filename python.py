def tenup(x):
    if x>10:
        return 10
    else:
        return x

def solution(cards):
    mycard=tenup(cards[0])+tenup(cards[2])
    dealer=tenup(cards[1])+tenup(cards[3])
    index=4
    if (cards[3]==1 or cards[3]>7):
        while mycard<17:
            mycard+=tenup(cards[index])
            index+=1
    elif(cards[3]==2 or cards[3]==3):
        while mycard<12:
            mycard+=tenup(cards[index])
            index+=1
    if mycard==21:
        return 3
    if mycard>21:
        return -2
    while dealer>17:
        dealer+=tenup(cards[index])
        index+=1
    if dealer>21:
        return 2

    mycard = 21-mycard
    dealer = 21-dealer
    if mycard<dealer:
        return 2
    elif dealer<mycard:
        return -2
    else:    
        return 1

print(solution([12, 7, 11, 6, 2, 12]))