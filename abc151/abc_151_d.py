from sys import stdin
import queue

H, W = [int(x) for x in stdin.readline().rstrip().split()]
maze = [stdin.readline().rstrip().split()[0] for _ in range(H)]

ans = 0

for h in range(H):
    for w in range(W):
        if maze[h][w] == '#':
            continue
        else:
            q = queue.Queue()
            q.put((h, w, 0))
            temp_h = h
            temp_w = w
            visited = [[0] * W for _ in range(H)]
            visited[h][w] = 1
            while q.qsize() > 0:
                temp = q.get()
                temp_h = temp[0]
                temp_w = temp[1]
                temp_d = temp[2]
                ans = max(ans, temp_d)
                visited[temp_h][temp_w] = 1
                if temp_h + 1 < H and maze[temp_h + 1][temp_w] == '.' and visited[temp_h + 1][temp_w] == 0:
                    # visited[temp_h + 1][temp_w] = 1
                    q.put((temp_h + 1, temp_w, temp_d + 1))
                if temp_h - 1 >= 0 and maze[temp_h - 1][temp_w] == '.' and visited[temp_h - 1][temp_w] == 0:
                    # visited[temp_h - 1][temp_w] = 1
                    q.put((temp_h - 1, temp_w, temp_d + 1))
                if temp_w + 1 < W and maze[temp_h][temp_w + 1] == '.' and visited[temp_h][temp_w + 1] == 0:
                    # visited[temp_h][temp_w + 1] = 1
                    q.put((temp_h, temp_w + 1, temp_d + 1))
                if temp_w - 1 >= 0 and maze[temp_h][temp_w - 1] == '.' and visited[temp_h][temp_w - 1] == 0:
                    # visited[temp_h][temp_w - 1] = 1
                    q.put((temp_h, temp_w - 1, temp_d + 1))

print(ans)
