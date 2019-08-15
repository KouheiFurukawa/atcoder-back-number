from sys import stdin
from collections import deque
import heapq


N, M = [int(x) for x in stdin.readline().rstrip().split()]
AB = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
AB.sort(key=lambda x: (x[0], -x[1]))
work = [deque([]) for _ in range(M + 1)]

for ab in AB:
    if ab[0] <= M:
        work[ab[0]].append(ab[1])

ans = 0
day = 1
available_work = []
while day <= M:
    for w in work[day]:
        heapq.heappush(available_work, -w)
    if len(available_work) > 0:
        ans += heapq.heappop(available_work)
    day += 1

print(-ans)
