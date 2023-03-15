n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
q = int(input())
W = list(map(int, input().split()))

C = []


for i in range(n):
    C.append(A[i]-B[i])

for i in W:
    count = 0
    for c in C:
        if c >= i:
            count += 1
        else:
            break
    print(count)
