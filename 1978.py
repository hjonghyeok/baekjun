import sys

n=map(int,sys.stdin.readline().rstrip())
m=list(map(int,sys.stdin.readline().rstrip().split()))
c=0
for i in m:
    if i == 1:
        continue
    for j in range(2,int(i**(1/2)+1)):
        if (i%j == 0):
            break
    else:
        c+=1
print(c)