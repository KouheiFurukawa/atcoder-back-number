from sys import stdin

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
S = stdin.readline().rstrip()
X = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(Q)]
cnt = [0] * (N + 1)
for i in range(N):
    if S[i:i + 2] == "AC":
        cnt[i + 1] = cnt[i] + 1
    else:
        cnt[i + 1] = cnt[i]
print(cnt)
for i, j in X:
    print(cnt[j - 1] - cnt[i - 1])
