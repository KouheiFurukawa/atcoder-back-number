from sys import stdin
from collections import deque
import math

m, n, s = [int(x) for x in stdin.readline().rstrip().split()]

xl = math.gcd(m, n)
X = []
c = 1
while c ** 2 <= xl:
    if xl % c == 0:
        X.append(c)
        X.append(xl // c)
    c += 1

cache = deque(maxlen=s)
X.sort()

A = [[0] * n for _ in range(m)]
B = [[0] * n for _ in range(n)]


def calc(p):
    cnt = 0
    for l in range(n // p):
        for i in range(m):
            for j in range(m):
                for k in range(p * l, p * (l + 1)):
                    if 'a,' + str(i) + ',' + str(k) not in cache:
                        cnt += 1
                        cache.append('a,' + str(i) + ',' + str(k))
                    if 'b,' + str(k) + ',' + str(j) not in cache:
                        cnt += 1
                        cache.append('b,' + str(k) + ',' + str(j))
    return cnt


ans = (10 ** 8, 0)
for k in X:
    c = calc(k)
    print(c)
    if c <= ans[0]:
        ans = (c, k)

print(ans[1])
