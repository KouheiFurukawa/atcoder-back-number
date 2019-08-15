from sys import stdin

N = int(stdin.readline().rstrip())
S = [stdin.readline().rstrip() for _ in range(N)]
count = {}

for s in S:
    s = ''.join(sorted(s))
    if s not in count:
        count[s] = 1
    else:
        count[s] += 1

ans = 0
for c in count:
    if count[c] > 1:
        ans += count[c] * (count[c] - 1) // 2

print(ans)
