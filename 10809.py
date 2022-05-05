import string
a = input()
b = string.ascii_lowercase
c = [-1]*len(b)
for i in a:
    c[b.index(i)] = a.index(i)
for i in c:
    print(i,end=" ")
