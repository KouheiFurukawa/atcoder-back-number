from sys import stdin
import math

N = int(stdin.readline().rstrip())
P = [int(x) for x in stdin.readline().rstrip().split()]
Q = [int(x) for x in stdin.readline().rstrip().split()]
rp = [int(x + 1) for x in range(N)]
rq = [int(x + 1) for x in range(N)]

index_p = 0
index_q = 0

for i in range(N):
    index_p += math.factorial(N - i - 1) * (rp.index(P[i]) - 1)
    index_q += math.factorial(N - i - 1) * (rq.index(Q[i]) - 1)
    rp.remove(P[i])
    rq.remove(Q[i])

print(abs(index_p - index_q))
