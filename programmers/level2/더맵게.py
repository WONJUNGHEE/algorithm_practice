import heapq

def solution(scoville, K):
    heap=scoville
    heapq.heapify(heap)
    answer = 0
    while(len(heap)>1):
        if(heap[0]<K):
            x=heapq.heappop(heap)
            y=heapq.heappop(heap)
            heapq.heappush(heap,x+y*2)
            answer+=1
            if(heap[0]>=K):
                return answer
        else:
            return answer

    return -1

a=[]
print(a[0])
