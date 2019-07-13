from sys import stdin
N = int(stdin.readline().rstrip())
A = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(2)]

dp = [[0] * N for _ in range(2)]
for n in range(N):
    dp[0][n] = sum(A[0][:n + 1])
dp[1][0] = A[0][0] + A[1][0]
for n in range(1, N):
    dp[1][n] = max(dp[0][n], dp[1][n - 1]) + A[1][n]
print(dp[1][N - 1])
