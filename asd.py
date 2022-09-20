import sys
n=int(sys.stdin.readline().rstrip())
list_n=list(map(int,sys.stdin.readline().rstrip().split()))
list_n1=sorted(set(list_n))

m=int(sys.stdin.readline().rstrip())
list_m=list(map(int,sys.stdin.readline().rstrip().split()))

def bynary_search(list_n1,k):
    left=0
    right=len(list_n1)-1
    while left<=right:
        mid=(left+right)//2
        if list_n1[mid]==k:
            return list_n.count(k)
        elif list_n1[mid]>k:
            right=mid-1
        else:
            left=mid+1
    return 0


for i in list_m:
    print(bynary_search(list_n1,i),end=" ")

