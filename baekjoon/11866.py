import collections

n,k= map(int,input().split())

people=collections.deque([i for i in range(1,n+1)])
delple=[]
count=0
while len(people)!=0:
    count+=1
    if count==k:
        delple.append(people[0])
        people.popleft()
        count=0
    else:
        people.rotate(-1)


print('<'+', '.join(map(str,delple))+'>')