from sys import stdin
import numpy as np
N = int(stdin.readline().rstrip())
P = np.array([int(stdin.readline().rstrip()) for _ in range(N)])
P = np.sort(P)
P = P[::-1]
P[0] = int(P[0] / 2)
print(np.sum(P))
