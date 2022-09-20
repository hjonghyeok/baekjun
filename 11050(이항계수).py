#이항계수
n, k = map(int, input().split())
def bino_coef(n,k):
    if k == 0 or k == n:
        return 1
    return bino_coef(n-1, k-1) + bino_coef(n-1, k)
print(bino_coef(n,k))