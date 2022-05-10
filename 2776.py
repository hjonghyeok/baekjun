import sys

t=int(sys.stdin.readline().rstrip())

def asd(k):
    left = 0
    right = len(a)-1
    while left<=right:
        mid = (left+right)//2
        if a[mid] == k:
            return 1
        elif a[mid] < k:
            left = mid+1
        else:
            right = mid-1
    return None


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    a=sorted(list(map(int,sys.stdin.readline().rstrip().split())))
    m = int(sys.stdin.readline().rstrip())
    b=list(map(int,sys.stdin.readline().rstrip().split()))
    for i in b:
        if asd(i):
            print(1)
        else:
            print(0)
