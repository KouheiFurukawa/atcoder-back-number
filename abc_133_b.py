from sys import stdin
N, D = [int(x) for x in stdin.readline().rstrip().split()]
X = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]

cnt = 0
for j in range(N):
    for k in range(j, N):
        dis = 0
        for d in range(D):
            dis += (X[j][d] - X[k][d]) ** 2
        if dis > 0 and (dis ** 0.5) % 1 == 0:
            cnt += 1

print(cnt)
