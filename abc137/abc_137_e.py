from sys import stdin

N, M, P = [int(x) for x in stdin.readline().rstrip().split()]
ABC = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(M)]

graph = [[] for _ in range(N)]

for abc in ABC:
    graph[abc[0] - 1].append((abc[1] - 1, P - abc[2]))


def bellman_ford(g, start):
    n = len(g)
    dist = [float("inf")] * n
    dist[start] = 0
    a0 = float("inf")

    for i in range(n << 1):
        updated = False
        for v in range(n):
            for to, cost in g[v]:
                if dist[to] <= dist[v] + cost:
                    continue
                dist[to] = dist[v] + cost
                updated = True
        if not updated:
            break
        if i <= n:
            a0 = dist[-1]
    if a0 != dist[-1]:
        return None, False
    return dist, True


dist, TF = bellman_ford(graph, 0)

if TF:
    print(max(-dist[-1], 0))
else:
    print(-1)
