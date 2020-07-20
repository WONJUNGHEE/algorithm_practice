import heapq

def solution(jobs):
    length=len(jobs)
    #jobs를 요청받은 시간 기준으로 내림차순한다. 
    jobs.sort(key =lambda x: x[0],reverse=True)
    index=0
    answer =0
    heap=[]
    while(len(jobs)!=0):
        for i in reversed(jobs):
            #디스크가 작업중이라면 heap에 저장한다.
            if index>=i[0]:
                heapq.heappush(heap,[i[1],i[0]])
                jobs.pop()
            else:
                break
        #디스크가 작업을 안하고 있을때 가장 빠른 입력이 시작한다.
        if(len(heap)==0):
            x=jobs.pop()
            heapq.heappush(heap,[x[1],x[0]])
            index=x[0]
        #힙에 들어있는것중 가장 빨리 끝나는 것을 실행 시킨다.   
        x=heapq.heappop(heap)
        index+=x[0]
        answer+=index-x[1]
    #jobs를 다 사용해서 heap에 남은것을 모두 동작 시킨다.
    while(heap):
        x=heapq.heappop(heap)
        index+=x[0]
        answer+=index-x[1]

    return answer//length
