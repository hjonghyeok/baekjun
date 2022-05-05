import sys

n = int(sys.stdin.readline().rstrip())
p = list(map(int,sys.stdin.readline().rstrip().split()))
p.sort()
sum=0
time=0
for i in p:
    sum += time+i
    time += i
print(sum)