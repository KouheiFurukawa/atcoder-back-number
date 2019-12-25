from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
ab = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N - 1)]
tree = [[] for _ in range(N)]

for i in range(N - 1):
    tree[ab[i][0] - 1].append(ab[i][1] - 1)
    tree[ab[i][1] - 1].append(ab[i][0] - 1)

q = deque([])
q.append(0)
colors = [[] for _ in range(N)]
ans = []
visited = [False] * N
cc = 0

while len(q) > 0:
    temp = q.popleft()
    visited[temp] = True
    cnt = 1
    for x in tree[temp]:
        if not visited[x]:
            q.append(x)
            while cnt in colors[temp]:
                cnt += 1
            colors[temp].append(cnt)
            colors[x].append(cnt)
            ans.append(cnt)


print(max(ans))
for i in ans:
    print(i)
