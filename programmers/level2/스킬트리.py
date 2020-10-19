    def solution(skill, skill_trees):
    answer = 0
    skill=list(skill)
    for i in skill_trees:
        i=list(i)
        first=[]
        flag=True
        for j in i:
            for k in skill:
                if j==k:
                    first.append(j)
        for i in range(len(first)):
            if skill[i]==first[i]:
                flag=True
            else:
                flag=False
                break
        if flag:
            answer+=1
            
                
    return answer