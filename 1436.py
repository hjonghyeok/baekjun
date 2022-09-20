a = []
for _ in range(9):
    a.append(int(input()))
for i in range(7):
    for j in range(i+1,9):
        if sum(a) - a[i] - a[j] == 100:
            a.remove(a[i])
            a.remove(a[j-1])
            break
    if len(a) == 7:
        break
for i in a:
    print(i)