import sys
n=int(sys.stdin.readline().rstrip())
a = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
a.sort(key=lambda x:x[0])
a.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(a[i][0], a[i][1])