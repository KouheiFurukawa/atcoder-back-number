from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
G = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(M)]
L = [G[k][0] for k in range(M)]
R = [G[k][1] for k in range(M)]
L.sort(reverse=True)
R.sort()
print(max(R[0] - L[0] + 1, 0))
