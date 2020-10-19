def solution(n, costs):
    answer = 0
    base = [0]*n
    #0번째 섬부터 돌기 위해 0번째 인덱스에 1
    base[0]=1
    #cost 기준으로 오름차순
    costs = sorted(costs,key=lambda x: x[2])
    
    #모든 섬을 돌았으면 종료
    while(sum(base)!=n):
        for i in costs:
            #0번째 섬부터 가는데 아무도 안간 섬이였으면 패스 
            if base[i[0]]==1 or base[i[1]]==1:
                #이미 두 섬을 돌았으면 컨티뉴
                if base[i[0]]==1 and base[i[1]]==1:
                    continue
                #안갔던 곳은 1로 하고 cost 만큼 더하기
                else: 
                    answer+=i[2]
                    base[i[0]]=1
                    base[i[1]]=1
                    break
            
                
    return answer