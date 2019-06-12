from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

n = int(stdin.readline().rstrip())
graph = [stdin.readline().rstrip().split()[2:] for _ in range(n)]
color = ['white'] * n
d = [0] * n
f = [0] * n
time_count = 0

adjacent_array = [[0] * n for x in range(n)]
for i in range(len(graph)):
    for j in graph[i]:
        adjacent_array[i][int(j)-1] = 1


def dfs(u):
    global time_count
    color[u] = 'gray'
    time_count += 1
    d[u] = time_count
    for v in range(len(adjacent_array[u])):
        if (adjacent_array[u][v] == 1) & (color[v] == 'white'):
            dfs(v)
    color[u] = 'black'
    time_count += 1
    f[u] = time_count


dfs(0)
print(d, f)
