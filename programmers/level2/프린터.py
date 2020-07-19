def solution(priorities, location):
    answer=1
    loc=location
    pri=priorities
    while(True):
        count=0
        for i in range(1,len(pri)):
            if(loc==0):
                if(pri[i]>pri[0]):
                    pri.append(pri[0])
                    loc=len(pri)-1
                    break
                count+=1
                if(count==len(pri)-1):
                    break
            else:
                if(pri[i]>pri[0]):
                    pri.append(pri[0])
                    break
                count+=1
                if(count==len(pri)-1):
                    answer+=1
        if(len(pri)==1):
            break
        pri.pop(0)
        loc-=1

    return answer

x=[3,3,4,2]

print(solution(x,3))