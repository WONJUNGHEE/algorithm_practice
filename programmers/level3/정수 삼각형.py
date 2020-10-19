
def solution(triangle):
    for x in range(1,len(triangle)):
        for y in range(x+1):
            if y==0:
                triangle[x][y]+=triangle[x-1][0]
            elif x==y:
                triangle[x][y]+=triangle[x-1][-1]
            else:
                triangle[x][y]+=max(triangle[x-1][y-1],triangle[x-1][y])
    return max(triangle[-1])
