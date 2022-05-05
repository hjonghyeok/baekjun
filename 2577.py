a = int(input())
b = int(input())
c = int(input())
sum = a*b*c
a_str = list(str(sum))
sum_int = "".join(map(str,a_str))

for i in range(10):
    print(sum_int.count(str(i)))
    