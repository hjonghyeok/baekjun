n = int(input())
a = int(input())
d = list(str(a))
b = list(map(int,d))
sum = 0

for i in b:
    sum += i
print(sum)