# 462A - Appleman and Easy Task

n = int(input())
string = ''
for i in range(n):
    string += input()
if string == string[::-1]:
    print("YES")
else:
    print("NO")