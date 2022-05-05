import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
a=[int(sys.stdin.readline().rstrip())for _ in range(n)]
c=0
for i in range(1,n+1):
    c += k//a[-i]
    k%=a[-i]
    if k<=0:
        break
print(c)