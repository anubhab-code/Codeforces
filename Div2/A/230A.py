s, n = list(map(int, input().split()))
flag = 0
l = []
for i in range(n):
    x, y = list(map(int, input().split()))
    l.append((x, y))
sorted(l)
if flag == 0:
    print("YES")
else:
    print("NO")
