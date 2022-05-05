import sys
n=int(sys.stdin.readline().rstrip())
a=[i for i in range(1,n+1)]
i=0
while True:
    i+=1
    if i>=len(a):
        break
    a.append(a[i])
    i+=1
print(a[-1])