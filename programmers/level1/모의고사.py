def solution(answers):
    answer = []
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    count1=0
    count2=0
    count3=0
    for i in range(len(answers)):
        if answers[i]==a1[i%5]:
            count1+=1
        if answers[i]==a2[i%8]:
            count2+=1 
        if answers[i]==a3[i%10]:
            count3+=1
    a=[count1,count2,count3]
    for count,i  in enumerate(a):
        if i==max(a):
            answer.append(count+1)
    return answer
z=[1,2,3,4,5]
solution(z)
