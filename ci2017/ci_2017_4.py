from sys import stdin
from collections import deque
m, n, s = [int(x) for x in stdin.readline().rstrip().split()]

cache = deque(maxlen=s)
cnt = 0

A = [[0] * n for _ in range(m)]
B = [[0] * n for _ in range(n)]

for i in range(m):
    for j in range(m):
        for k in range(n):
            print(cache)
            if 'a,' + str(i) + ',' + str(k) not in cache:
                cnt += 1
                cache.append('a,' + str(i) + ',' + str(k))
            if 'b,' + str(k) + ',' + str(j) not in cache:
                cnt += 1
                cache.append('b,' + str(k) + ',' + str(j))

print(cnt)
