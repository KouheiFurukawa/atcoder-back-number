from sys import stdin

# bfs practice
R, C = [int(x) for x in stdin.readline().rstrip().split()]
sy, sx = [int(x) for x in stdin.readline().rstrip().split()]
gy, gx = [int(x) for x in stdin.readline().rstrip().split()]

L = [[x for x in stdin.readline().rstrip()] for _ in range(R)]
q = [(sy - 1, sx - 1, 0)]
visit = []
now = (sy - 1, sx - 1, 0)
time_stamp = 0

while now[0] != gy - 1 or now[1] != gx - 1:
    now = q[0][:2]
    time_stamp = q[0][2]
    q.pop(0)
    visit.append(now)
    if (now[0] + 1, now[1]) not in visit and (now[0] + 1, now[1], time_stamp + 1) not in q and L[now[0] + 1][now[1]] == '.':
        q.append((now[0] + 1, now[1], time_stamp + 1))
    if (now[0] - 1, now[1]) not in visit and (now[0] - 1, now[1], time_stamp + 1) not in q and L[now[0] - 1][now[1]] == '.':
        q.append((now[0] - 1, now[1], time_stamp + 1))
    if (now[0], now[1] + 1) not in visit and(now[0], now[1] + 1, time_stamp + 1) not in q and  L[now[0]][now[1] + 1] == '.':
        q.append((now[0], now[1] + 1, time_stamp + 1))
    if (now[0], now[1] - 1) not in visit and (now[0] + 1, now[1], time_stamp - 1) not in q and L[now[0]][now[1] - 1] == '.':
        q.append((now[0], now[1] - 1, time_stamp + 1))
    if now[0] == gy - 1 and now[1] == gx - 1:
        print(time_stamp)
