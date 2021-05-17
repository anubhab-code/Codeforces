# 224A - Parallelepiped

import math
a,b,c = list(map(int,input().split()))
val = 4*math.sqrt(a*b*c)*((1/a)+(1/b)+(1/c))
print(round(val))