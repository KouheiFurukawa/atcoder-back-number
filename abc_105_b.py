from sys import stdin
import math

N = int(stdin.readline().rstrip())

for k in range(math.floor(N / 7) + 1):
    if (N - 7 * k) % 4 == 0:
        print('Yes')
        break
    if k == math.floor(N / 7):
        print('No')
