from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
S = [int(x) for x in stdin.readline().rstrip().split()]
T = [int(x) for x in stdin.readline().rstrip().split()]

dp = [1] * (M+1)
acc = [0] * M

for s in S:
    ndp = [1]
    for i, t in enumerate(T):
        if s == t:
            ndp.append(ndp[-1] + dp[i+1])
            acc[i] = dp[i+1]
        else:
            ndp.append(ndp[-1] + acc[i])
        print(ndp)
    dp = ndp

print(dp[-1] % (10 ** 9 + 7))
