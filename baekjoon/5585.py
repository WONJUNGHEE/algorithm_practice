import sys

def change(n):
    global count
    for i in changes:
        if n>i:
            n=n-i
            count+=1
            change(n)
            break
        elif n==i:
            count+=1
            break

    return count

if __name__ =="__main__":
    n=int(sys.stdin.readline())
    changes=[500,100,50,10,5,1]
    count=0
    print(change(1000-n))
