def solution(progresses, speeds):
    answer = []
    day=[]
    for i in range(len(progresses)):
        x=100-progresses[i]
        remain=0
        if x%speeds[i] != 0:
           remain+=1 
        remain+=x//speeds[i]
        day.append(remain)
    max=day[0]
    count=0
    for i in day:
        if max>=i:
            count+=1
        else:
            answer.append(count)
            max=i
            count=1
    answer.append(count)
    return answer