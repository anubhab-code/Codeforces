# 296A - Yaroslav and Permutations

n = int(input())
l = list(map(int, input().split()))
unique = set(l)
flag = 1
for i in unique:
  if (l.count(i)*2)-1 > n:
    flag = 0
if flag == 1:
  print("YES")
else:
  print("NO")
