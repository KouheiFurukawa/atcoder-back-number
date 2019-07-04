import numpy as np

w = int(input())
n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

# dp[N][W]
dp = np.zeros((k + 1, w + 1))

for i in range(n):
    a, b = ab[i]
    if a > w:
        continue
    print(dp)
    print(dp[1:, a:])
    print(dp[:k, :w + 1 - a])
    dp[1:, a:] = np.maximum(dp[:k, :w + 1 - a] + b, dp[1:, a:])

print(dp)
print(int(dp[k, w]))
