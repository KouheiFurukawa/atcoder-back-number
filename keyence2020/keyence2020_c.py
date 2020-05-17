from sys import stdin

N, K, S = [int(x) for x in stdin.readline().rstrip().split()]

ans = [S] * K
if S == 10 ** 9:
    ans.extend([1] * (N - K))
else:
    ans.extend([S + 1] * (N - K))

print(*ans)
