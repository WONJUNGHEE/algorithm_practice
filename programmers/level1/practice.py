def solution(inputString):
    count1=0
    count2=0
    count3=0
    count4=0
    total=0
    for i in inputString:
        if(i=='('):
            count1+=1
            total+=1
        if(i=='['):
            count2+=1
            total+=1
        if(i=='<'):
            count3+=1
            total+=1
        if(i=='{'):
            count4+=1
            total+=1
        if(i==')'):
            count1-=1
        if(i==']'):
            count2-=1
        if(i=='>'):
            count3-=1
        if(i=='}'):
            count4-=1
        if(count1 < 0 or count2 < 0 or count3 < 0 or count4 < 0):
            return -1

    return total