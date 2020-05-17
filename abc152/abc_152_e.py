from sys import stdin
from collections import defaultdict

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

mod = 10 ** 9 + 7
g = defaultdict(int)
ans = 0

for i in range(N):
    tmp = 1
    a = A[i]
    g_tmp = defaultdict(int)
    while tmp <= A[i] ** 0.5:
        while tmp > 1 and a % tmp == 0:
            a //= tmp
            if tmp not in g_tmp:
                g_tmp[tmp] = 1
            else:
                g_tmp[tmp] += 1
        tmp += 1
    if a > 1:
        if a not in g_tmp:
            g_tmp[a] = 1
        else:
            g_tmp[a] += 1

    for j in g_tmp:
        if j not in g:
            g[j] = g_tmp[j]
        else:
            g[j] = max(g[j], g_tmp[j])

l = 1
ans = 0
for i in g:
    l *= pow(i, g[i], mod)
    l %= mod
for a in A:
    ans += l * pow(a, mod - 2, mod)
    ans %= mod

print(ans)