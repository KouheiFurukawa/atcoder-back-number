from sys import stdin

W = int(stdin.readline().rstrip())
N, K = [int(x) for x in stdin.readline().rstrip().split()]
shot = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
dp = [[0] * (W + 1) for k in range(N + 1)]

for i in range(N):
    print(dp)
    for w in range(W):
        if w + 1 >= shot[i][0]:
            dp[i + 1][w + 1] = max(dp[i + 1][w + 1], dp[i][w + 1 - shot[i][0]] + shot[i][1])
        dp[i + 1][w + 1] = max(dp[i][w + 1], dp[i + 1][w + 1])

print(dp)

# N = int(stdin.readline().rstrip())
# dp = [k for k in range(N + 1)]
#
# for n in range(N + 1):
#     i = 0
#     j = 0
#     while 6 ** i <= n:
#         dp[n] = min(dp[n], dp[n - 6 ** i] + 1)
#         i += 1
#     while 9 ** j <= n:
#         dp[n] = min(dp[n], dp[n - 9 ** j] + 1)
#         j += 1
#
# print(dp[N])
