from sys import stdin


N, K = [int(x) for x in stdin.readline().rstrip().split()]
P = [int(x) for x in stdin.readline().rstrip().split()]

D = sum(P[:K])
index = 0
ans = D

for i in range(1, N - K + 1):
    if D + P[i + K - 1] - P[i - 1] > ans:
        ans = D + P[i + K - 1] - P[i - 1]
    D = D + P[i + K - 1] - P[i - 1]
print((ans + K) / 2)
