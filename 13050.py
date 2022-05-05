import sys
n=int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().rstrip().split()))
b = list(map(int,sys.stdin.readline().rstrip().split()))
m = 0
i=0
oil=0
mm=1000000000
su = sum(a)
mi = min(b[:-1])
while True:
    if mi >= b[0]:
        print(su*b[0])
        break
    if mi < b[i]:
        if mm>b[i]:
            m += int(mm*oil)
            if oil!=0:
                oil=0
            oil += a[i]
            su -= a[i]
            mm = b[i]
        else:
            oil += a[i]
            su -= a[i]
    else:
        m += mm*oil
        m += int(b[i]*su)
        print(m)
        break
        i+=1

