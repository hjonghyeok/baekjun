a,b,c=map(int,input().split())
d=int(input())
c+=d
print((a+b//60)%24,(b+c//60)%60,c%60,end=" ")