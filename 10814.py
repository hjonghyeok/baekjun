import sys
n=int(sys.stdin.readline().rstrip())
m=[]
for _ in range(n):
    a,b=map(str,sys.stdin.readline().rstrip().split())
    a = int(a)
    m.append((a,b))
m.sort(key=lambda x:x[0])

for i in range(n):
    print(m[i][0],m[i][1])