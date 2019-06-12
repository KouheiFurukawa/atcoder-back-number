from sys import stdin
import queue

n = int(stdin.readline().rstrip())
graph = [stdin.readline().rstrip().split()[2:] for _ in range(n)]
d = [10 ** 7] * n
color = ['white'] * n
q = queue.Queue()

adjacent_matrix = [[0] * n for x in range(n)]
for i in range(len(graph)):
    for j in graph[i]:
        adjacent_matrix[i][int(j)-1] = 1


def bfs(s):
    d[s] = 0
    q.put(s)
    while not q.empty():
        u = q.get()
        print(u)
        for v in range(len(adjacent_matrix[u])):
            if (adjacent_matrix[u][v] == 1) & (color[v] == 'white'):
                color[v] = 'gray'
                d[v] = d[u] + 1
                q.put(v)
        color[u] = 'black'


bfs(0)
print(d)
