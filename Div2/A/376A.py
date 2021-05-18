# 376A - Lever

string = input().split('^')
left, right = 0, 0
for i in range(len(string[0])):
    if string[0][i] in '123456789':
        left += (len(string[0]) - i) * int(string[0][i])
for i in range(0, len(string[1])):
    if string[1][i] in '123456789':
        right += (i+1) * int(string[1][i])
if left == right:
    print("balance")
elif left > right:
    print("left")
else:
    print("right")
