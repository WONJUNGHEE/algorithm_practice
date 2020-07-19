def solution(n, lost, reserve):
    answer = n-len(lost)
    a=reserve
    b=lost
    for i in range(len(b)):
        for j in range(len(reserve)):
            if b[i]==reserve[j]:
                answer+=1
                b[i]=50
                a[j]=99
                break
            
    for i in range(len(b)):
        for j in range(len(reserve)):
            if b[i]==reserve[j]+1:
                answer+=1
                a[j]=99
                break
            elif b[i]==reserve[j]-1:
                answer+=1
                a[j]=99
                break

    return answer