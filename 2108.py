import sys

n = int(sys.stdin.readline().rstrip())
m = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
m.sort()
print(round(sum(m)/n))
print(m[n//2])
a = [[i,0] for i in range(-4000,4001)]
for i in m:
    a[i+4000][1] += 1
a.sort(key=lambda x:(-x[1],x[0]))
if n==1:
    print(m[0])
else:
    if a[0][1] != a[1][1]:
        print(a[0][0])
    else:
        print(a[1][0])
print(max(m)-min(m))
