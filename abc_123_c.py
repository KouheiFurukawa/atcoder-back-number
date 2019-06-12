from sys import stdin
import numpy as np

N = int(stdin.readline().rstrip())
S = np.array([int(stdin.readline().rstrip()) for _ in range(5)])
P = np.array([N, 0, 0, 0, 0, 0])
cnt = 0

while P[5] != N:
    n = np.array([min(S[k], P[k]) for k in range(5)])
    n = np.append(n, 0)
    n = np.append(0, n)
    P = P - n[1:]
    P = P + n[:-1]
    cnt += 1


print(cnt)
