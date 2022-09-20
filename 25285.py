import sys
t = int(sys.stdin.readline().rstrip())
n = []
for _ in range(t):
    cm, kg = map(int, sys.stdin.readline().rstrip().split())
    bmi = (kg / (cm * cm))*10000
    if cm < 140.1:
        n.append(6)
    elif cm >= 140.1 and cm < 146:
        n.append(5)
    elif cm >= 146 and cm < 159:
        n.append(4)      
    elif cm >= 159 and cm < 161:
        if bmi >= 16 and bmi < 35:
            n.append(3)
        else:
            n.append(4)
    elif cm >= 161 and cm < 204:
        if bmi >= 20 and bmi < 25:
            n.append(1)
        elif (bmi >= 18.5 and bmi < 20) or (bmi >= 25 and bmi < 30):
            n.append(2)
        elif (bmi >= 16 and bmi < 18.5) or (bmi >= 30 and bmi < 35):
            n.append(3)
        else:
            n.append(4)
    else:
        n.append(4)

for _ in n:
    print(_)