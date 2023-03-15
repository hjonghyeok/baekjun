n = int(input())
c = 1
b = 1
s = 0
if n == 1:
    print(1)
else:
    for i in range(1,n):
        s += 1
        if s > 6*c:
            s = 0
            c += 1
    print(c+1)