from sys import stdin
import heapq

N, M = [int(x) for x in stdin.readline().rstrip().split()]
B = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(M)]

graph = [[] for _ in range(N)]
for i in range(1, N):
    graph[i].append((0, i - 1))
for m in B:
    graph[m[0] - 1].append((m[2], m[1] - 1))

d = [(0, 0)]
distance = [10 ** 15] * N
distance[0] = 0
color = ['white'] * N
heapq.heapify(d)

while len(d) > 0:
    temp, u = heapq.heappop(d)
    color[u] = 'black'
    if distance[u] < temp:
        continue
    for v in graph[u]:
        if color[v[1]] != 'black':
            if distance[u] + v[0] < distance[v[1]]:
                distance[v[1]] = distance[u] + v[0]
                color[v[1]] = 'gray'
                heapq.heappush(d, (distance[v[1]], v[1]))

if distance[N - 1] == 10 ** 15:
    print(-1)
else:
    print(distance[N - 1])
