n,m=input().split()
count=0
index = len(m) - len(n)+1
Min=50
for i in range(index):
    diff=0
    for j in range(len(n)):
        if n[j] != m[i+j]:
            diff+=1
    if diff<Min:
        Min = diff

print(Min)