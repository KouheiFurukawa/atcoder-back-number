from sys import stdin
N, M = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
BC = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(M)]
BC.sort(key=lambda x: x[1], reverse=True)
for i in range(M):
    A.extend([BC[i][1]] * BC[i][0])
    if len(A) >= 2 * N:
        break

A.sort(reverse=True)
print(sum(A[:N]))
