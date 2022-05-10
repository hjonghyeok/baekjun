import sys
n = int(sys.stdin.readline().rstrip())
a=sorted(list(map(int,sys.stdin.readline().rstrip().split())))
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

m = int(sys.stdin.readline().rstrip())
b=list(map(int,sys.stdin.readline().rstrip().split()))
c=[0]*len(b)
for i in range(len(b)):
    if asd(b[i]):
        c[i]+=1

for i in c:
    print(i,end=" ")
    

