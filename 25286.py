import sys

t = int(sys.stdin.readline().rstrip())
k = []
for _ in range(t):
    y, m = map(int, sys.stdin.readline().rstrip().split())
    M = [y,m,m]
    M[2] -= m
    if M[2]<1:
        M[1] -= 1
        if M[1]<1:
            M[1] = 12
            M[0] -= 1
        if M[1] == 1 or M[1] == 3 or M[1] == 5 or M[1] == 7 or M[1] == 8 or M[1] == 10 or M[1] == 12:
            M[2] += 31
        elif M[1] == 4 or M[1] == 6 or M[1] == 9 or M[1] == 11:
            M[2] += 30
        else:
            if (M[0]%100 != 0 and M[0]%4 == 0) or M[0]%400 == 0:
                M[2] += 29
            else:
                M[2] += 28
    k.append(M)

for _ in k:
    print(_[0], _[1], _[2])