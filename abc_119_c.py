from sys import stdin
N, A, B, C = [int(x) for x in stdin.readline().rstrip().split()]
l = [int(stdin.readline().rstrip()) for _ in range(N)]


def dfs(k, p, q, r):
    if k == N:
        if min(p, q, r) > 0:
            print(k, p, q, r)
            print(abs(p - A)+abs(q - B)+abs(r - C) - 30)
            return abs(p - A)+abs(q - B)+abs(r - C) - 30
        else:
            return 10 ** 7
    t1 = dfs(k + 1, p, q, r)
    t2 = dfs(k + 1, p + l[k], q, r) + 10
    t3 = dfs(k + 1, p, q + l[k], r) + 10
    t4 = dfs(k + 1, p, q, r + l[k]) + 10
    return min(t1, t2, t3, t4)


print(dfs(0, 0, 0, 0))
