from sys import stdin
from collections import deque

H, W = [int(x) for x in stdin.readline().rstrip().split()]
B = [list(stdin.readline().rstrip()) for _ in range(H)]

q = deque([])

for k in range(H):
    for l in range(W):
        if B[k][l] == '#':
            q.append((k, l, 0))

while len(q) > 0:
    h, w, t = q.popleft()
    if h > 0:
        if B[h - 1][w] == '.':
            B[h - 1][w] = '#'
            q.append((h - 1, w, t + 1))
    if h < H - 1:
        if B[h + 1][w] == '.':
            B[h + 1][w] = '#'
            q.append((h + 1, w, t + 1))
    if w > 0:
        if B[h][w - 1] == '.':
            B[h][w - 1] = '#'
            q.append((h, w - 1, t + 1))
    if w < W - 1:
        if B[h][w + 1] == '.':
            B[h][w + 1] = '#'
            q.append((h, w + 1, t + 1))
    if len(q) == 0:
        print(t)

