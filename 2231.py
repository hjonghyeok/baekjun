import sys
a=int(sys.stdin.readline().rstrip())
for i in range(1,a):
    b=list(str(i))
    b=list(map(int,b))
    if (i+sum(b))==a:
        print(i)
        break
else:
    print(0)