r= open('input.txt','rt')
number= int(r.readline())
x=[]
count=0
while(number != 0):
    number-=1
    k=int(r.readline())
    if k==0:
        x.pop()
    else:
        x.append(k)

for i in x:
    count+=i

print(count)
            
