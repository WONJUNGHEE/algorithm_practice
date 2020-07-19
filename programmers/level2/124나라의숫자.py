def solution(n):
    answer=0
    number=[4,1,2]
    div=n    
    mod=1
    while(True):
        ddd=div%3
        answer+=number[ddd]*mod
        div=div//3
        
        if (div==1 and ddd==0):
            break
        if div==0:
            break
        if ddd==0:
            div-=1
        mod=mod*10

    return str(answer)