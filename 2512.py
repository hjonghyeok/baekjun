import sys

n = int(sys.stdin.readline().rstrip())
a=sorted(list(map(int,sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())

for i in range(n):
    if (m/(n-i)) >= a[i]:
        m-=a[i]
    else:
        k = int(m/(n-i))
        print(k)
        break
else:
    print(max(a))