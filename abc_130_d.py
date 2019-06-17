from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
a = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0
cnt = 0
Sum = 0
bottom = 0
while True:
    if Sum < K:
        Sum += a[cnt]
        cnt += 1
    if Sum >= K:
        ans += N - cnt + 1
        Sum -= a[bottom]
        bottom += 1
    if cnt == N and Sum < K:
        break

print(ans)
