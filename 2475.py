a=list(map(int,input().split()))
b=[]
sum = 0
for i in a:
    b.append(i*i)
for i in b:
    sum += i
print(sum%10)