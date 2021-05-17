# 43A - Football

n = int(input())
d = {}
for _ in range(n):
    team = input()
    if team in d.keys():
        d[team]+=1
    else:
        d[team]=1
m = float("-inf")
win = ''
for i in d.keys():
    if d[i] > m:
        m = d[i]
        win = i
print(win)
    