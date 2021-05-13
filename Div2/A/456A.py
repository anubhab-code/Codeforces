# 456A - Laptops

n = int(input())
l = []
for i in range(n):
    l.append(tuple(list(map(int,input().split()))))
first = sorted(l)
second = sorted(l,key = lambda x:x[1])
flag = 0
for i in range(n):
    if first[i]!=second[i]:
        flag = 1
if flag == 1:
    print("Happy Alex")
else:
    print("Poor Alex")