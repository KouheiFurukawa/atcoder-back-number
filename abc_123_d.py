from sys import stdin
import heapq

X, Y, Z, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]
C = [int(x) for x in stdin.readline().rstrip().split()]

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

heap = []
heapq.heappush(heap, (-(A[0] + B[0] + C[0]), 0, 0, 0))
print(heap)
s = {(0, 0, 0)}
for _ in range(K):
    v, i, j, k = heapq.heappop(heap)
    if i + 1 < X and (i + 1, j, k) not in s:
        s.add((i + 1, j, k))
        heapq.heappush(heap, (-(A[i + 1] + B[j] + C[k]), i + 1, j, k))
    if j + 1 < Y and (i, j + 1, k) not in s:
        s.add((i, j + 1, k))
        heapq.heappush(heap, (-(A[i] + B[j + 1] + C[k]), i, j + 1, k))
    if k + 1 < Z and (i, j, k + 1) not in s:
        s.add((i, j, k + 1))
        heapq.heappush(heap, (-(A[i] + B[j] + C[k + 1]), i, j, k + 1))
    print(-v)
