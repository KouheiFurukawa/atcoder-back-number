from sys import stdin
N, T = [int(x) for x in stdin.readline().rstrip().split()]
ct = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(N)]
path = [k[0] for k in ct if k[1] <= T]
path.sort()
if len(path) == 0:
    print('TLE')
else:
    print(path[0])
