from collections import Counter
def solution(clothes):
    cloth_list = []
    for i in clothes:
        cloth_list.append(i[1])
    answer = Counter(cloth_list)
    if len(answer)==1:
        return list(answer.values())[0]
    else:
        ret = 1 
        for v in list(answer.values()):
            ret *= (v+1)
    return ret-1