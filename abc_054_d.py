def calc():
    n, ma, mb = map(int, input().split())
    dp = [[0] * 401 for _ in range(401)]
    for _ in range(n):
        a, b, c = map(int, input().split())
        for i in range(400, -1, -1):
            for j in range(400, -1, -1):
                if i - a < 0 or j - b < 0:
                    continue
                else:
                    if dp[i - a][j - b] == 0:
                        continue
                    else:
                        if dp[i][j] == 0:
                            dp[i][j] = dp[i - a][j - b] + c
                        else:
                            dp[i][j] = min(dp[i][j], dp[i - a][j - b] + c)
        if dp[a][b] == 0:
            dp[a][b] = c
        else:
            dp[a][b] = min(dp[a][b], c)
    ans = 10 ** 10
    for i in range(401):
        if i * ma > 400 or i * mb > 400:
            break
        if dp[i * ma][i * mb] == 0:
            continue
        else:
            ans = min(ans, dp[i * ma][i * mb])
    if ans == 10 ** 10:
        print(-1)
    else:
        print(ans)


calc()
