import sys
n=int(sys.stdin.readline().rstrip())
b=[0]*10001
for i in range(n):
    b[int(sys.stdin.readline().rstrip())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)