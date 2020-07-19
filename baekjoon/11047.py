import sys
def change_coin(n):
    global count
    for money in money_list:
        if n>money: 
            count+= n//money
            n=n%money
        elif n%money==0:
            count+=n//money
            break
    return count

if __name__ =="__main__":
    n, total_coin=list(map(int,sys.stdin.readline().strip().split()))
    money_list=[]
    count =0
    for i in range(n):
        coin = int(sys.stdin.readline().strip())
        if coin > total_coin:
            break
        money_list.append(coin)
    money_list=list(reversed(money_list))
    print(change_coin(total_coin))
