# 276A - Lunch Rush

n,k = list(map(int,input().split()))
joy = []
for i in range(n):
    f,t = list(map(int,input().split()))
    if t > k:
        joy.append(f-(t-k))
    else:
        joy.append(f)
print(max(joy))