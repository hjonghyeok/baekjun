import sys

n = int(sys.stdin.readline().strip())
m = []
count = []
sum =0

def ccw(x1,y1,x2,y2,x3,y3):
    tem = (x1-x2)*(y3-y2) - (x3-x2)*(y1-y2)
    if tem >0:
        return 1
    elif tem <0:
        return -1
    else:
        return 0

for i in range(n):
    m.append(list(map(int, sys.stdin.readline().strip().split())))
m.sort(key=lambda x: x[4])

for i in range(n-1):
    c=0
    for j in range(i,n-1):
        if (i+j)>=n:
            break
        if ccw(m[i][0],m[i][1],m[i][2],m[i][3],m[i+j][0],m[i+j][1]) <0 and ccw(m[i][0],m[i][1],m[i][2],m[i][3],m[i+j][2],m[i+j][3]) <0:
            c += 1
        count.append(c)
count.append(0)
for i in range(n):
    sum += m[i][4] * (count[i]+1)
print(sum)