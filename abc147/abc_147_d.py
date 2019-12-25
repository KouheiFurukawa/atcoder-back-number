from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

inf = 10 ** 9 + 7

cnt = [0] * 60

for a in A:
    s = bin(a)[2:].zfill(60)
    s = s[::-1]
    for i in range(60):
        if s[i] == '1':
            cnt[i] += 1

ans = 0
for i in range(60):
    ans += (cnt[i] * (N - cnt[i])) * (2 ** i)
    ans %= inf

print(ans)
