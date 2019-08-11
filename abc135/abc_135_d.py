from sys import stdin

S = stdin.readline().rstrip()

inf = 10 ** 9 + 7
dp = [0] * 13
dp[0] = 1
dres = 1

for s in reversed(S):
    ndp = [0] * 13
    for res in range(13):
        candidate = range(10) if s == '?' else [int(s)]
        for digit in candidate:
            nres = (dres * digit + res) % 13
            ndp[nres] = (ndp[nres] + dp[res]) % inf
    print(dp)
    dp = ndp
    dres = (dres * 10) % 13

print(dp[5])
