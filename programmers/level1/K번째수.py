def solution(array, commands):
    answer = []
    for i in commands:
        a=[] 
        for j in range(i[0],i[1]+1):
            a.append(array[j-1])
        a.sort()
        answer.append(a[i[2]-1])     
    return answer
