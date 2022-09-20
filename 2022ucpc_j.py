import sys

n = int(sys.stdin.readline().strip())
m = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    for j in range(i+1,n):
        if m[i]< m[j]:
            break
        if ((m[i]*m[j])**0.5)%1==0:
            if m[i]>m[j]:
                m[i],m[j]=m[j],m[i]
                break
for i in range(n-1):
    if m[i]>m[i+1]:
        print("NO")
        break
else:
    print("YES")
