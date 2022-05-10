import sys
a=[0]*10
for i in range(10):
    a[i]=int(sys.stdin.readline().rstrip())%42
print(len(set(a)))
