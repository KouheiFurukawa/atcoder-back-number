from sys import stdin
from collections import defaultdict

N = int(stdin.readline().rstrip())
S = [stdin.readline().rstrip() for i in range(N)]

D = defaultdict(int)

for s in S:
    D[s] += 1

ans = sorted(D.items(), key=lambda x: (-x[1], x[0]))

for a in ans:
    if a[1] < ans[0][1]:
        break
    print(a[0])


