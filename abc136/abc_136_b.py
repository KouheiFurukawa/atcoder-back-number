from sys import stdin

N = int(stdin.readline().rstrip())

ans = 0
digit = len(str(N))
for i in range(digit):
    if i % 2 == 1:
        ans += 10 ** i - 10 ** (i - 1)

if digit % 2 == 1:
    ans += N - 10 ** (digit - 1) + 1

print(ans)
