c = int(input())
a = [0]*c
for i in range(c):
    count = 0;sum = 0
    n = list(map(int, input().split()))
    for j in range(1,n[0]+1):
        sum += n[j]
    avr = sum/n[0]
    for j in range(1,n[0]+1):
        if avr < n[j]:
            count += 1
    a[i] = count/n[0]*100
for i in a:
    print('%.3f%%'%i)