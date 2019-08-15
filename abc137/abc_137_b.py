from sys import stdin

K, X = [int(x) for x in stdin.readline().rstrip().split()]
ans = [x for x in range(max(X - (K - 1), -1000000), min(X + K, 1000001))]
print(*ans)
