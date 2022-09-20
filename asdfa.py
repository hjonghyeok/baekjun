import sys

n = int(sys.stdin.readline().strip())
m = map(str, sys.stdin.readline().strip().split())
q = [0] * n
k = []
for i in range(n):
    k.append(list(map(str, sys.stdin.readline().strip().split())))
k1 = sum(k,[])
k1 = list(k1)
for i in range(n):
    q[i] = k1.count(m[i])
        
print(q)
