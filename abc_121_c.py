from sys import stdin
N, M = [int(x) for x in stdin.readline().rstrip().split()]
X = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
X.sort(key=lambda x: x[0])
ans = 0
for k in range(N):
    if M == 0:
        break
    buy = min(X[k][1], M)
    M -= buy
    ans += buy * X[k][0]
print(ans)
