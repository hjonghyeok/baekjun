import sys

n, k = map(int,sys.stdin.readline().rstrip().split())
count = 0 # 날짜 카운터
c = 1 # 에어컨 켜진횟수 카운터
hh = 15 # 시
mm = 0 # 분
h=[]
m=[]


while True:
    if count == n:
        break
    if c<=3:
        hh += 3
        c += 1
        if mm >= 60:
            hh += (mm//60)
            mm %= 60
        if hh>=24:
            count += (hh//24)
            hh %= 24
    else:
        hh += 15
        mm += k
        c = 1
        if mm >= 60:
            hh += (mm//60)
            mm %= 60
        if hh>=24:
            count += (hh//24)
            hh %= 24

while True:
    if c<=3:
        h.append(hh)
        m.append(mm)
        hh += 3
        c += 1
        if mm >= 60:
            hh += (mm//60)
            mm %= 60
        if hh>=24:
            break
    else:
        hh += 15
        mm += k
        c = 1
        if mm >= 60:
            hh += (mm//60)
            mm %= 60
        if hh>=24:
            break

print(len(h))
for i in range(len(h)):
    print('%02d'%h[i],end=":"'%02d\n'%m[i])