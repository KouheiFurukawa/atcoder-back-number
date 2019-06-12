from sys import stdin
N, K = [int(x) for x in stdin.readline().rstrip().split()]
h = [int(stdin.readline().rstrip()) for _ in range(N)]
h.sort()
diff = [h[k + K - 1] - h[k] for k in range(N - K + 1)]
diff.sort()
print(diff[0])
