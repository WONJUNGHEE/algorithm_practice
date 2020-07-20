import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    #배열 거꾸로 하기
    dates=dates[::-1]
    supplies=supplies[::-1]
    heap=[]
    #stock 이 k 넘어가면 종료
    while(stock<k):
        #dates 뒤에서 부터 출력
        for i in reversed(dates):
            if stock>=i:
                dates.pop()
                #힙은 최소힙이 기본이기 때문에 최대힙으로 하기 위해 -를 붙인다
                heapq.heappush(heap,-supplies.pop())
            else:
                break
        # 최대힙에 -를 다시 붙여 최대값을 더 한다.
        stock+=-heapq.heappop(heap)
        answer+=1
    return answer