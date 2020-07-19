from itertools import combinations

def solution(n):
    a=[1,3]
    three=3
    my=[3]
    if(n==1):
        return 1
    while(len(a)<=n-1):
        three*=3
        a.append(three)
        my.append(three)
        
        b=list(combinations(a,2))
        for i in range(len(b)):
            my.append(b[i][0]+b[i][1])
        b=list(combinations(a,3))
        for i in range(len(b)):
            my.append(b[i][0]+b[i][1]+b[i][2])
    my.sort()
    my_set=set(my)
    new_list=list(my_set)
    zz=sorted(new_list)
    return zz[n-2]

print(solution(100))