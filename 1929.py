import sys

m,n=map(int,sys.stdin.readline().rstrip().split())
a = 0
for i in range(m,n+1):
    if i == 1:
        continue
    for j in range(2,int(i**(1/2)+1)):
        a=0
        if (i%j == 0):
            a = 1
            break
    else:
        print(i)