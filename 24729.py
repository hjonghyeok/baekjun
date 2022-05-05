import sys

a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
i = 0
sw = 0
j = 0
while j < a and i < a-1:
    if (b[i] - b[j] == 1) or (b[i] - b[j] == -1):
        sw = b[i+1]
        b[i+1] = b[j]
        b[j] = sw
        i += 1
        j = i
    j += 1
    
if (b[0] - b[a-1] != 1) and (b[0] - b[a-1] != -1):
    print(-1)
else:
    for i in range(a-1):
        if (b[i] - b[i+1] != 1) and (b[i] - b[i+1] != -1):
            print(-1)
            break
    else:
        print(1)
