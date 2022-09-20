import sys

n = int(sys.stdin.readline().strip())
temp = []
k = []
v = []
for i in range(n):
   v.append(list(map(int,sys.stdin.readline().strip().split())))
   
u = sorted(list(v))
c = u[n-1][0]
for i in range(n-2,0,-1):
    k.append(i)
    if u[i][0] == c:
        continue
    else:
        c = u[i][0]
        k.append(i)

# for i in range(n):
#     temp = u[i]
#     for j in range(i+1,n):
#         if u[i][0] == u[j][0]:
#             if temp[1] < u[j][1]:
#                 temp = u[j]
#         else:
#             break  
#     k.append(v.index(temp)+1)
print(sum(set(k)))