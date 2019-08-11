from collections import deque
from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
uv = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(M)]
S, T = [int(x) for x in stdin.readline().rstrip().split()]

graph = [[] for _ in range(N)]
for x in uv:
    graph[x[0] - 1].append(x[1] - 1)

ans = -1
queue = deque()
queue.append([S - 1, 0])
visited = {S - 1: 1}
visited2 = {}

print(graph)
while queue != deque():
    tmp = queue.popleft()
    print(tmp)
    if tmp[0] == T - 1:
        ans = tmp[1]
        break
    tmp_queue = deque()
    tmp_queue.append(tmp[0])
    for i in range(3):
        tmp2_queue = tmp_queue
        tmp_queue = deque()
        for j in tmp2_queue:
            if (j, i) in visited2:
                continue
            else:
                visited2[j, i] = 1
                tmp_queue += graph[j]
    print(tmp_queue)
    for i in tmp_queue:
        if i in visited:
            continue
        else:
            visited[i] = 1
            queue.append([i, tmp[1] + 1])

print(ans)
