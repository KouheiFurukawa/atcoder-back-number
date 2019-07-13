from sys import stdin, exit

N = int(stdin.readline().rstrip())
s = [int(stdin.readline().rstrip()) for _ in range(N)]
dp = [0] * (100 * N)
dp[0] = 1
for n in range(N):
    for p in range(len(dp) - 1, 0, -1):
        if p - s[n] >= 0:
            if dp[p - s[n]] == 1 and 0 <= p:
                dp[p] = 1
for k in range(len(dp)):
    if dp[len(dp) - k - 1] == 1 and (len(dp) - k - 1) % 10 != 0:
        print(len(dp) - k - 1)
        exit()
print('0')
