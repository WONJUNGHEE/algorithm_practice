# 효휼성 불통
def solution(people, limit):
    answer=0
    peo=people
    peo.sort(reverse=True)
    while(len(peo)!=0):
        if len(peo)==1:
            answer+=1
            break
        if (peo[0] +peo[len(peo)-1])<=limit:
            peo.remove(peo[len(peo)-1])
            peo.remove(peo[0])
            answer+=1
        else:
            peo.remove(peo[0])
            answer+=1
    return answer
# 정답
def solution(people,limit):
    people.sort()
    length=len(people)
    light=0
    heavy=length-1
    count=0
    while(light<heavy):
        if people[light]+people[heavy]<=limit:
            count+=1
            light+=1
            heavy-=1
        else:
            heavy-=1
    return length-count
