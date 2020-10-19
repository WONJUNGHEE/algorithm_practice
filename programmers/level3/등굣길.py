def solution(m, n, puddles):
    array=[[0]*(m+1) for i in range(n+1)]
    array[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if( i==1 and j==1):
                continue
            if[j,i] in puddles:
                array[i][j]=0
            else:
                array[i][j]=array[i-1][j]+array[i][j-1]

    print(array)
    return array[n][m]%1000000007


print(solution(4,3,[[2,2]]))