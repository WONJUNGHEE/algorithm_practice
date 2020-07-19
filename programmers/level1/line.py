import numpy as np
def solution(snapshots, transactions):
    account={}
    account2={}
    answer=[]
    transactions = list([transactions[0]])
    for i in range(len(snapshots)):
        acc=snapshots[i][0]
        money=int(snapshots[i][1])
        account[acc]=money
    for i in range(len(transactions)):
        if(transactions[i][1]=="SAVE"):
            acc=transactions[i][2]
            money=int(transactions[i][3])
            account[acc]=account.get(acc,0) + money
        if(transactions[i][1]=="WITHDRAW"):
            acc=transactions[i][2]
            money=int(transactions[i][3])
            account[acc]=account.get(acc,0)-money
    print(account)
    return answer