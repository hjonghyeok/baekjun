N = int(input())

for _ in range(N):
    a = int(input())
    if a <= 2:
        print('No')
    elif a % 2 == 0:
        print('No')
    else:
        for i in range(3, int((a-2)**0.5)+1, 2):
            if a % i == 0:
                print('No')
                break
        else:
            print('Yes')