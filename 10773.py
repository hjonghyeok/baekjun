import sys
k=int(input())
a=[]
for i in range(k):
    n=int(sys.stdin.readline())
    if n==0:
        del a[-1]
    else:
        a.append(n)
print(sum(a))