import sys

if __name__ == '__main__':
    n = int(input())
    M = list(map(int, sys.stdin.readline().split()))
    aa = 0
    K = []
    if n == 1:
        M.sort()
        for i in range(5):
            aa += M[i]
    else:
        K.append(min(M[0],M[5]))
        K.append(min(M[1],M[4]))
        K.append(min(M[2],M[3]))
        K.sort()
        m1 = K[0]
        m2 = K[0]+K[1]
        m3 = sum(K)
        n3 = 4
        n2 = 4 * (n - 1) + 4 * (n - 2)
        n1 = 4 * (n - 2) * (n - 1) + (n - 2) ** 2
        aa = n1*m1+n2*m2+n3*m3
    print(aa)
