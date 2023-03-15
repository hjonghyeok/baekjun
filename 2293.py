n, k = map(int, input().split())

A = list(int(input()) for _ in range(n))

DP = [0] * 10001
DP[0] = 1

for i in A:
    for j in range(1, k+1):
        if j - i >= 0:
            DP[j] += DP[j - i]

print(DP[k])
    