while True:
    text=input()
    if text =='.':
        break
    stack_list=[]
    check = 1
    for j in text:
        if(j=='('):
            stack_list.append(0)
        elif(j=='['):
            stack_list.append(1)
        elif(j==')'):
            if len(stack_list)==0:
                check=0
                break
            if stack_list.pop() != 0:
                check=0
                break
        elif (j==']'):
            if len(stack_list)==0:
                check=0
                break
            if stack_list.pop()!=1:
                check=0
                break
    if len(stack_list)==0 and check:
        print("yes")
    else:
        print("no")
