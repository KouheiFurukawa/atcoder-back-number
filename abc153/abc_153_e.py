from sys import stdin

H, N = [int(x) for x in stdin.readline().rstrip().split()]
AB = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
AB.sort(reverse=True, key=lambda x: x[0])
dp = [[10 ** 9] * (N + 1) for _ in range(H + AB[0][0] + 1)]

for k in range(N + 1):
    dp[0][k] = 0

for i in range(len(dp)):
    for j in range(N):
        cnt = 0

        if i - AB[j][0] >= 0:
            dp[i][j + 1] = min(dp[i - AB[j][0]][j + 1] + AB[j][1], dp[i][j])
        else:
            dp[i][j + 1] = dp[i][j]

ans = 10 ** 9

for i in range(H, len(dp)):
    for j in range(N + 1):
        ans = min(ans, dp[i][j])

print(ans)
