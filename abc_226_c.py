from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
P = 0
for i in range(1, N + 1):
    if i > K:
        continue
    e = 0
    while i * 2 ** e < K:
        P += 1 / N * 0.5 ** (e + 1)
        e += 1
print(1 - P)
