from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
x = [int(x) for x in stdin.readline().rstrip().split()]


ans = 100000000000
#最初と最後だけ調べればOK
for i in range(N - K + 1):
    tmp_min = x[i]
    tmp_max = x[i + K - 1]
    print(tmp_min, tmp_max)
    print(abs(tmp_max) + abs(tmp_min - tmp_max))
    ans = min(ans, min(abs(tmp_min), abs(tmp_max)) + abs(tmp_min - tmp_max))
print(ans)
