import sys
n = int(sys.stdin.readline().rstrip())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(sys.stdin.readline().rstrip())
sum = 0
mo = 0
m1 = m
a.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    sum += (a[i][0])
sum += (-2*(n-1))-1
    
for i in range(n):
    mo += a[i][1]
    if m <= (a[i][0]-1):
        m -= (a[i][0]-1)
    else:
        m -= (a[i][0]-2)
    if m<=0:
        break
if sum < m1:
    print(-1)
else:
    print(mo)
