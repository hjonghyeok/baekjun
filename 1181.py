import sys
n = int(sys.stdin.readline().rstrip())
a = [sys.stdin.readline().rstrip()for _ in range(n)]
b = sorted(set(a))
b.sort(key=len)
for i in b:
    print(i)
