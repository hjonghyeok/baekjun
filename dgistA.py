
import sys

n, k = map(int,sys.stdin.readline().rstrip().split())
day = 0 # 날짜 카운터
c = 1 # 에어컨 켜진횟수 카운터
hh = 15 # 시
mm = 0 # 분
h=[]
m=[]


while True:
    if day == n: #선택한 날짜에 탈출!
        break 
    if c<=3: # 에어컨 카운터가 3회 이하면 실행
        hh += 3
        c += 1
        if mm >= 60:
            hh += (mm//60)
            mm %= 60
        if hh>=24:
            day += (hh//24)
            hh %= 24
    else: # 에어컨 카운터가 3회 초과면 실행
        hh += 15
        mm += k
        c = 1 # 카운터 초기화
        if mm >= 60:
            hh += (mm//60)
            mm %= 60
        if hh>=24:
            day += (hh//24)
            hh %= 24

while True:
    if c<=3: # 카운트가 3회 이하일때 실행
        h.append(hh)
        m.append(mm)
        hh += 3
        c += 1
        if mm >= 60:
            hh += (mm//60)
            mm %= 60
        if hh>=24: # 날짜가 넘어가면 탈출
            break
    else: # 카운트가 3회 초과일때 실행
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
    