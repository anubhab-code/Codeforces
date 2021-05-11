#144A - Arrival of the General

n = int(input())
data = list(map(int,input().split()))
rev = data[::-1]
min_ = rev.index(min(data))
max_ = data.index(max(data))
min_ = n-1-min_
if min_ < max_:
    print((n-min_-1)+(max_)-1)
else:
    print((n-min_-1)+(max_))