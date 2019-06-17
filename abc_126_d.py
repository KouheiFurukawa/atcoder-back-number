from sys import stdin

N = int(stdin.readline().rstrip())
tree = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
ans = [-1] * N
edge = [[] * N]
for k in range(N - 1):
    tree[k][0] -= 1
    tree[k][1] -= 1
    tree[k][2] %= 2

    edge[tree[k][0]].append((tree[k][1], tree[k][2]))
    edge[tree[k][1]].append((tree[k][0], tree[k][2]))
stack = [(x, 0) for x in edge[0]]
ans[0] = 0
while len(stack) > 0:
    e, c = stack.pop()
    n, w = e[0], e[1]
    if ans[n] >= 0:
        continue
    ans[n] = (c + w) % 2
    stack += [(k, ans[n]) for k in edge[n]]

print(ans)

