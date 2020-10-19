def solution(people, limit):
    answer=0
    light=0
    people.sort()
    peo = len(people)-1
    while(light<peo):
        if(people[light]+people[peo]<=limit):
            peo-=1
            answer+=1
            light+=1
        else:
            peo-=1
            answer+=1
    return answer