from itertools import permutations

def solution(numbers):
    answer=0
    number=[]
    for i in range(1,len(numbers)+1):
        #i 길이 만큼의 조합을 만든다
        combination=list(permutations(numbers,i))
        for n in combination:
            number.append(int(''.join(n)))
    number=list(set(number))

    #소수찾기
    while(number):
        flag = True
        x= number.pop()
        if x==1 or x==0:
            continue
        for i in range(2,x):
            if x%i ==0:
                flag=False
                break
        if flag ==True:
            answer+=1

    return answer
    