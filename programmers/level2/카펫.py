def solution(brown, yellow):
    #yellow 세로가 1일때
    if(yellow<=3):
        expectbro= (yellow+2)*2 +2
        if expectbro==brown:
            return [yellow+2,3]
    #가로 길이가 더 커야하기 때문에 가로에 큰값으로 하기
    for row in range(1,yellow//2+1):
        if yellow%row ==0:
            width=yellow//row
            length=row
    #brown 값이랑 yellow 가로 세로 길이를 했을때 예측한 brown 값이 같은면 리턴
            expectbro= (width+2)*2 +length*2
            if expectbro==brown:
                return [width+2,length+2]