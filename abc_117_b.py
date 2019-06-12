from sys import stdin
import numpy as np
N = int(stdin.readline().rstrip())
L = np.array([int(x) for x in stdin.readline().rstrip().split()])
LS = np.sort(L)[::-1]
if LS[0] < np.sum(LS[1:]):
    print('Yes')
else:
    print('No')
