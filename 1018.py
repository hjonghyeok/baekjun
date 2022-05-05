import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
a = [sys.stdin.readline().rstrip() for _ in range(n)]
for i in range(len(a)):
    a[i] = list(a[i])
b = a[0][0]
c = 0

def swap(k,h):
        if a[k][h] == 'W':
            a[k][h] = 'B'
        else:
            a[k][h]= 'W'

for i in range(1,n,2):
    if a[i][0] == b:
        c += 1
        swap(i,0)
    
for i in range(2,n,2):
    if a[i][0] != b:
        c += 1
        swap(i,0)

for i in range(n):
    for j in range(1,m,2):
        if a[i][0] == a[i][j]:
            c+=1
            swap(i,j)
    for j in range(2,m,2):
        if a[i][0] != a[i][j]:
            c+=1
            swap(i,j)
for i in range(n):
    print(a[i])
print(c)