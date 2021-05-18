# 437A - The Child and Homework

choice = ['A', 'B', 'C', 'D']
size = []
min_, max_, great, index = float("inf"), float("-inf"), 0, 0
for i in range(4):
    ch = input()[2:]
    size.append((len(ch), i+1))
    min_, max_ = min(len(ch), min_), max(len(ch), max_)
size.sort()
if min_ <= size[1][0]//2:
    great += 1
    index = size[0][1]
if max_ >= size[-2][0]*2:
    great += 1
    index = size[-1][1]
if great == 1:
    print(choice[index-1])
else:
    print("C")
