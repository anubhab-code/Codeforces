a,b,c = int(input()) , int(input()) , int(input())
print(max(list(map(eval, ['(a+b)+c', 'a+(b+c)', '(a*b)+c','a*(b+c)', '(a+b)*c', 'a+(b*c)', 'a*b*c']))))