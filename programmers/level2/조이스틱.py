def solution(name):
    alpabet = list(name)
    allA=["A"]*len(alpabet)
    answer = 0
    index=0
    left=0
    right=0

    while(True):
        # alpabet이 13번 이상이면 아래키로 뒤에서부터 찾기
        if(ord(alpabet[index])-65>13):
            answer+=90-ord(alpabet[index])+1
        else:
            answer+=ord(alpabet[index])-65
        alpabet[index]='A'

        #alpabet 이 모두 'A'면 종료
        if alpabet==allA:
            break

        left =right = index
        move=0
        #인덱스 기준 앞이나 뒤에 'A'값이 아니면 인덱스 옮기기 만약 둘다면 왼쪽으로
        while True:
            left -=1
            right+=1
            move+=1
            if left < 0:
                left = len(alpabet)-1
            if right >len(alpabet)-1:
                right=0
            if alpabet[right] !='A':
                index =right
                answer+=move
                break
            elif alpabet[left] !='A':
                index = left
                answer+=move
                break


    return answer