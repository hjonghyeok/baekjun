import sys
n=int(sys.stdin.readline().rstrip())
m=list(map(int,sys.stdin.readline().rstrip().split()))
a=list(sorted(set(m)))

dic = {a[i]:i for i in range(len(a))}

for i in m:
    print(dic[i],end=" ")
