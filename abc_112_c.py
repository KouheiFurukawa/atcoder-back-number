from sys import stdin
N = int(stdin.readline().rstrip())
X = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
X.sort(key=lambda x: x[2])
a, b, c = X[-1]

for px in range(101):
    for py in range(101):
        H = abs(a - px) + abs(b - py) + c
        for k in range(N):
            if X[k][2] != max(H - abs(X[k][0] - px) - abs(X[k][1] - py), 0):
                break
            if k == N - 1:
                print(px, py, H)

