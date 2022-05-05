t=int(input())
a=[]
for i in range(t):
    h,w,n = map(int,input().split())
    k = n%h
    z = int(n//h+1)
    a.append([k,z])
for i in range(t):
    print(a[i][0],end='')
    print(str(a[i][1]).zfill(2))