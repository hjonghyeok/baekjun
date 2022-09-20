
import sys
b=[]
while 1:
    a = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    if a[2]**2 == a[0]**2 + a[1]**2:
        b.append('right')
    else:
        b.append('wrong')
for i in b:
    print(i)