from sys import stdin

s = stdin.readline().rstrip()
ans = 0
for k in range(len(s)):
    ans += int(s[len(s) - k - 1]) * (4 ** k)
print(ans)
