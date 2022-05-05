import sys
n = int(sys.stdin.readline())
a = sorted(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

def search(target):
    left = 0
    right = len(a)-1
    
    while left<=right:
        mid = (left+right)//2
        if a[mid] == target:
            return 1
        elif a[mid]>target:
            right = mid-1
        else:
            left = mid+1

for i in range(m):
    if search(b[i]):
        print(1)
    else:
        print(0)