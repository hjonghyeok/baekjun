import sys

n=int(sys.stdin.readline().rstrip())
avr=list(map(int,sys.stdin.readline().rstrip().split()))
m=max(avr)
for i in range(n):
    avr[i]=avr[i]/m*100

print(sum(avr)/n)
    