import sys
n=int(sys.stdin.readline())
number =list(map(int,sys.stdin.readline().strip().split()))
number.sort()
total_time=0
waiting_time=0
for time in number:
    waiting_time+=time
    total_time+=waiting_time
print(total_time)
