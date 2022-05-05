import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
b = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

sum = 0
for i in range(len(b)):
    sum += a[-(i+1)] - b[i]
    
print(sum)
