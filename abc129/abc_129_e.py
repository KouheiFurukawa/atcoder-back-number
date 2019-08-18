from sys import stdin

L = stdin.readline().rstrip()
inf = 10 ** 9 + 7
ones = 3
if L[-1] == '0':
    ans = 1
else:
    ans = 3

if len(L) == 1:
    print(ans)
    exit()

for i in range(2, len(L) + 1):
    if L[-i] == '1':
        ans = (ones + 2 * ans) % inf
    ones = (3 * ones) % inf

print(ans)
