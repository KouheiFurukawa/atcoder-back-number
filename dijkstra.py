from sys import stdin
import numpy as np

N = int(stdin.readline().rstrip())
X = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]

inf = 10 ** 7
adjacent_array = np.full((N, N), inf)
d = np.full(N, inf)
color = ['white'] * N
p = np.zeros(N)
mincost = inf

for k in range(N):
    for l in [2 * x + 3 for x in range(int((len(X[k]) - 2) / 2))]:
        adjacent_array[k][X[k][l - 1]] = X[k][l]


def dijkstra(s):
    d[s] = 0
    p[s] = -1
    u = 0
    global mincost

    while True:
        mincost = inf
        for i in range(N):
            if (color[i] != 'black') & (d[i] < mincost):
                mincost = d[i]
                u = i
        if mincost == inf:
            break
        print(str(u) + ' ' + str(mincost))
        color[u] = 'black'
        for v in range(N):
            if (color[v] != 'black') & (adjacent_array[u][v] < inf):
                if d[u] + adjacent_array[u][v] < d[v]:
                    d[v] = d[u] + adjacent_array[u][v]
                    p[v] = u
                    color[v] = 'gray'


dijkstra(0)
