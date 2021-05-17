# 488A - Giga Tower


def lucky(n):
    digits = [int(x) for x in str(n)]
    if 8 in digits:
        return True
    return False


n = int(input())
copy = n+1
while not lucky(abs(copy)):
    copy += 1
print(copy-n)
