import heapq

def solution(operations):
    answer = []
    heap=[]
    for i in operations:
        x= i.split()
        if x[0]=="I":
            heapq.heappush(heap,int(x[1]))
        elif len(heap)==0:
            continue
        elif x[0]=="D":
            if x[1]=="-1":
                heapq.heappop(heap)
            elif x[1]=="1":
                heap.pop()
        heap.sort()
    
    if heap:
        return [heap[-1],heap[0]]
    else:
        return [0,0]
        

    return answer
