n = int(input())
m = [int(x) for x in input().split()]
v = int(input())
count = 0
for i in m:
    if i == v:
        count += 1
print(count)