from sys import stdin

s = 'abcdefgh'
x = stdin.readline().rstrip()
ans = 0

for k in range(len(x)):
    ans += s.index(x[len(x) - k - 1]) * (8 ** k)

print(ans)
