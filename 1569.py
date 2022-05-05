import sys
n=int(sys.stdin.readline().rstrip())
x=[]
y=[]
for _ in range(n):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    x.append(a)
    y.append(b)
if max(x)-min(x) == max(y)-min(y):
    print(max(x)-min(x))
else:
    print(-1)