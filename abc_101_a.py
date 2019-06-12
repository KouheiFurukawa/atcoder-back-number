from sys import stdin
S = stdin.readline().rstrip()

n = 0
for k in S:
    if k == '+':
        n += 1
    else:
        n -= 1

print(n)
