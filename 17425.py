import sys
MAX = 1000000
dp = [1]*(MAX+1)
s=[0]*(MAX+1)

for i in range(2,MAX+1):
    j=1
    while i*j<=MAX:
        dp[i*j] += i
        j += 1
for i in range(1,MAX+1):
    s[i] = s[i-1]+dp[i]
    
n=int(sys.stdin.readline())
b=[]
for i in range(n):
    t=int(sys.stdin.readline())
    b.append(s[t])
print('\n'.join(map(str,b))+'\n')