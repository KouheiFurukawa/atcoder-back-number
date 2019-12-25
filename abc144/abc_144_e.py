from sys import stdin
import heapq

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
F = [int(x) for x in stdin.readline().rstrip().split()]
Q = []
A.sort(reverse=True)
F.sort()
print(A)
print(F)
for i in range(N):
    if K == 0:
        break
    k = min(A[i] - A[-1], K)
    A[i] -= k
    K -= k

A.sort(reverse=True)
ans = 0

for i in range(N):
    ans = max(A[i] * F[i], ans)

print(ans)
