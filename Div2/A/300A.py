# 300A - Array

n = int(input())
l = list(map(int, input().split()))
a, b, c = [], [], []
for i in l:
	if i < 0:
		a.append(i)
	elif i > 0:
		b.append(i)
	else:
		c.append(i)
if not b:
	b.append(a.pop())
	b.append(a.pop())
if len(a) % 2 == 0:
	c.append(a.pop())
print(len(a), *a)
print(len(b), *b)
print(len(c), *c)
