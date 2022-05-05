import imp


import sys
a = list(map(int,sys.stdin.readline().split()))
count = 0
for i in range(8):
    if count>a[i]:
        count = a[i]
    elif count<a[i]:
        