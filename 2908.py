a, b = map(int,input().split())
a_1 = list(str(a))
a_1.reverse()
a = int("".join(map(str,a_1)))
b_1 = list(str(b))
b = int("".join(map(str,b_1[::-1]))) #b_1[::-1] == b_1.reverse()

if a>b:
    print(a)
else:
    print(b)


# print(max(input()[::-1].split()))
# 위랑 같음