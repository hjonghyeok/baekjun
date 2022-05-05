n = int(input())
a = list(map(int,input().split()))
b = [0]*n

for i in range(n):
    for j in range(i):
        if a[i]>a[j] and b[i]<b[j]:
            b[i]=b[j]
    b[i] += 1
print(max(b))#리스트b중에 최대값 출력