def solution(routes):
    routes.sort()
    answer = 0
    base =[0]*len(routes)
    for i in range(len(routes)-1,-1,-1):
        #카메라를 입구 설치 한다.
        if(base[i]==0):
             camera=routes[i][0]
             answer+=1
        for j in range(i,-1,-1):
            #카메라를 안 지나쳤고 거리 사이에 카메라가 있으면 체크한다.
            if base[j]==0 and routes[j][1] >= camera >= routes[i][0]:
                base[j]=1
    return answer