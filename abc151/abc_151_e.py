from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) for x in stdin.readline().rstrip().split()]

A.sort()
c = 1
ans = 0
inf = 10 ** 9 + 7
fact_list = [1] * (N + 1)
fact_inv = [1] * (N + 1)
f = 1

for i in range(1, N + 1):
    f *= i
    f %= inf
    fact_list[i] = f

for i in range(1, N + 1):
    fact_inv[i] = pow(fact_list[i], inf - 2, inf)

for i in range(N - K + 1):
    tmp_min = A[i]
    tmp_max = A[N - i - 1]
    d = (tmp_max - tmp_min) % inf
    n = fact_list[N - i - 1] * fact_inv[K - 1] * fact_inv[N - i -K] % inf
    ans += d * n
    ans %= inf

print(int(ans))
