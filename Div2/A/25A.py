# 25A - IQ test

n = int(input())
data = list(map(int,input().split()))
modified = [ x%2 for x in data]
even = modified.count(0)
odd = modified.count(1)
for i in range(len(data)):
    if odd == 1:
        if data[i]%2==1:
            print(i+1)
            break
    elif even == 1:
        if data[i]%2==0:
            print(i+1)
            break
        