a = [i for i in range(1,10001)]
b = []
for i in a:
    if i<10:
        b.append(i+i)
    elif i<100:
        b.append(i+(i%10)+(i//10))
    elif i<1000:
        b.append(i+(i//100)+(i%100//10)+(i%10))
    elif (i<10000) and (i+(i//1000)+(i%1000//100)+(i%100//10)+(i%10)) <= 10000:
        b.append(i+(i//1000)+(i%1000//100)+(i%100//10)+(i%10))
        
for i in set(b):
    a.remove(i)
for i in a:
    print(i)