from sys import stdin
import numpy as np

H, W = [int(x) for x in stdin.readline().rstrip().split()]
S = [stdin.readline().rstrip() for _ in range(H)]
S_new = np.array([[1 if S[k][l] == '#' else 0 for l in range(W)] for k in range(H)])
up = np.zeros((H, W))
down = np.zeros((H, W))
left = np.zeros((H, W))
right = np.zeros((H, W))

for y in range(H):
    cnt = 0
    for x in range(W - 1):
        if S_new[y][x] == 0:
            cnt += 1
        else:
            cnt = 0
        left[y][x + 1] = cnt
    cnt = 0
    for x in range(W - 1):
        if S_new[y][W - x - 1] == 0:
            cnt += 1
        else:
            cnt = 0
        right[y][W - x - 2] = cnt

for x in range(W):
    cnt = 0
    for y in range(H - 1):
        if S_new[:, x][y] == 0:
            cnt += 1
        else:
            cnt = 0
        up[y + 1][x] = cnt
    cnt = 0
    for y in range(H - 1):
        if S_new[:, x][H - y - 1] == 0:
            cnt += 1
        else:
            cnt = 0
        down[H - y - 2][x] = cnt

sums = np.array([[up[y][x] + down[y][x] + left[y][x] + right[y][x] + 1 if S_new[y][x] == 0 else 0 for x in range(W)] for y in range(H)])
print(int(sums.max()))
