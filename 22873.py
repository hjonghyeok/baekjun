import sys
import time
n, q = map(int, sys.stdin.readline().split())
a = int(input())
b = int(input())
start = time.time()
c = a+b
a_l = [0]*n
b_l = [0]*n
c_l = [0]*(n+1)
c2_l = [0]*(n+1)
count = [0] * q
f_l = [0] * q
i_int = [0] * q
d_l = [0] * q


def func1(k_str, k_l): #리스트로 변환
    for j in range(1,len(k_str)+1):
        k_l[-j] = k_str[-j]

def func2(k_l):#리스트를 문자열, 정수로 변환
    return "".join(map(str,k_l)), int("".join(map(str,k_l)))
    

a_str = list(str(a))
func1(a_str,a_l)        
b_str = list(str(b))
func1(b_str,b_l)
    
# for j in range(q):   
#     f, i, d = input().split()
#     i_int = int(i)

#     c_str = list(str(c))
#     func1(c_str,c_l)
        
#     if f == 'B':
#         b_l[-i_int] = d
#     elif f == 'A':
#         a_l[-i_int] = d
        
#     a_str, a_int = func2(a_l)
#     b_str, b_int = func2(b_l)
    
#     c2 = a_int+b_int
#     c2_str = list(str(c2))
#     func1(c2_str,c2_l)
    
#     for k in range((n+1)):
#         if c2_l[k] != c_l[k]:
#             count[j] += 1
    
#     c_str, c_int = func2(c_l)
#     c2_str, c2_int = func2(c2_l)
    
#     c = c2       

for j in range(q):        
    f, i, d = sys.stdin.readline().split()
    f_l[j] = f
    i_int[j] = int(i)
    d_l[j] = d
    
for j in range(q):
    c_str = list(str(c))
    func1(c_str,c_l)
        
    if f_l[j] == 'B':
        b_l[-i_int[j]] = d_l[j]
    elif f_l[j] == 'A':
        a_l[-i_int[j]] = d_l[j]
        
    a_str, a_int = func2(a_l)
    b_str, b_int = func2(b_l)
    
    c2 = a_int+b_int
    c2_str = list(str(c2))
    func1(c2_str,c2_l)
    
    for k in range((n+1)):
        if c2_l[k] != c_l[k]:
            count[j] += 1
    
    c_str, c_int = func2(c_l)
    c2_str, c2_int = func2(c2_l)
    
    c = c2        

for j in count:
    print(j)
end = time.time()
print(end-start)
