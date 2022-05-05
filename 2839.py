import sys

n = int(sys.stdin.readline().rstrip())

if n%5%3 == 0:
    print((n//5)+n%5//3)
else:
    if (n%3) != 0:
        print(-1)
    else:
        print(n//3)
