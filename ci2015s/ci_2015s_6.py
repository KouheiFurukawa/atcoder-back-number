S = [s.replace('\n', '') for s in open('../sample.txt').readlines()]
ans_cnt = 0


def compare(s, t):
    maxl = 0
    if len(s) < 20 or len(t) < 20:
        return 10 ** 8
    dp = [[0] * (len(t) + 1) for x in range(len(s) + 1)]
    for x in range(1, len(s) + 1):
        for y in range(1, len(t) + 1):
            if s[x - 1] == t[y - 1]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            elif dp[x - 1][y] >= dp[x][y - 1]:
                dp[x][y] = dp[x - 1][y]
            elif dp[x][y - 1] >= dp[x - 1][y]:
                dp[x][y] = dp[x][y - 1]
            maxl = max(maxl, dp[x][y])
    return max(len(s), len(t)) - maxl


for j in range(len(S) - 1):
    for k in range(j + 1, len(S)):
        if compare(S[j], S[k]) < 4:
            print(S[j])
            print(S[k])
            ans_cnt += 1

print(ans_cnt)
