import sys

q = int(sys.stdin.readline().strip())
m = []
k = []
y = 0

def f(x):
    sum = 1
    for i in range(0,len(k),2):
        sum *= x*k[i] + k[i+1]
    return sum

for i in range(q):
    m = (list(map(int, sys.stdin.readline().strip().split())))
    if m[0] == 1:
        k.append(m[1])
        k.append(m[2])
    if m[0] == 2:
        y = f(m[1])
        if y < 0:
            print("-")
        elif y == 0:
            print(0)
        else:
            print("+")