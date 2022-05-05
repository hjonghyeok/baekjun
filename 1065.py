import sys
n=int(sys.stdin.readline().rstrip())

f = 99
if n<100:
    f=n
elif (n >=100) and (n<1000):
    for i in range(100,n+1):
        a = i//100
        b = (i%100)//10
        c = i%10
        if (a-b) == (b-c):
            f+=1
else:
    f = 144
print(f)