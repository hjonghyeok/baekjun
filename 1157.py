a=input().upper()
b = list(set(a))
d = [a.count(i) for i in b] # 알파벳 개수를 d에 저장
if d.count(max(d))>1: #d에서 가장 큰 값이 2개 이상이면
    print('?')
else:
    print(b[d.index(max(d))]) #d에 가장 큰 값의 인덱스

# d.sort()
# c = d[-1]
# b = [a[i] for i in range(len(a)) if a.count(a[i])<c]
# a = set(a)
# for i in b:
#     a.remove(i)
# if len(a) >1:
#     print("?")
# else:
#     print("".join(map(str,a)))

