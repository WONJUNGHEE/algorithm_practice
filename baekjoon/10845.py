r= open('input.txt','rt','uft-8')
number= int(r.readline())
x=[]
while(number != 0):
    number-=1
    cmd = r.readline()
    if cmd.split()[0]=='push':
        print(x.append(cmd.split(' ')[1]))
    elif cmd=='pop':
        if not x:
            print(-1)
        else:
            print(x.pop())
    elif cmd == 'front':
        if not x:
            print(-1)
        else:
            print(x[0])
    elif cmd == 'back':
        if not x:
            print(-1)
        else:
            print(x[0])
    elif cmd == 'empty':
        if not x:
            print(1)
        else:
            print(0)
    elif cmd == 'size':
        print(len(x))
