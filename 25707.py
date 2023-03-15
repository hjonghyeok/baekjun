n = int(input())
m = sorted(list(map(int, input().split())))
s = 0
for i in range(len(m)-1):
    s += m[i+1]-m[i]
s += m[-1]-m[0]
print(s)