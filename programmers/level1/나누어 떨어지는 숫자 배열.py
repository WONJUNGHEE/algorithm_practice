def solution(arr, divisor):
    answer = []

    for j in arr:
        if j%divisor==0:
            answer.append(j)
            answer.sort()
    
    if answer==[]:
        answer.append(-1)
    return answer