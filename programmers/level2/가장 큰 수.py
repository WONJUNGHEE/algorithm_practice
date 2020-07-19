def solution(numbers):
    numbers=list(map(str,numbers))
    answer= ''.join(sorted(numbers,lambda x: x*3,reverse=True))
    return answer
