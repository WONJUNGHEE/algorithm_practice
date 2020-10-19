class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        arr=[]
        for i in range(len(mat)):
            check=0
            for j in mat[i]:
                check+=j
            if check ==1:
                arr.append(i)
        answer=0
        for k in arr:
            sum=0
            for row in range(len(mat[0])):
                if mat[k][row]==1:
                    for col in range(len(mat)):
                        sum+=mat[col][row]
                        if(sum>1):
                            break
                    if(sum==1):
                        answer+=1
                    break
        return answer
