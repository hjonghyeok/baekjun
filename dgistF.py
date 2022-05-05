import sys
n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
st = [0]*n
i = 0
happy = 0
while True:
    if st[n-1]==2:
        break
    happy += p[i]
    st[i]+=1
    i+= 1
    if i == len(p):
        i = 0 
print(happy)    
