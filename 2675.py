import sys
t = int(sys.stdin.readline())
q = [""]*t

for i in range(t):
    a, b = sys.stdin.readline().split()
    a_int = int(a)
    c = list(str(b))
    for j in c:
        q[i] += j*a_int
for i in q:
    print(i)
