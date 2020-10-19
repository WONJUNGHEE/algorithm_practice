def solution(weights):
    weights.sort()
    temp = weights[0]
    #부분합을 이용한 문제  나는 못품
    #부분합으로 해서 weight[i]까지 숫자가 안나오면 거기까지가 최솟값이다
    for i in range(1, len(weights)):
        if weights[i] - temp > 1:
            break
        else:
            temp += weights[i]
    
    return temp + 1