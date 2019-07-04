from sys import stdin

# ABC
# N = int(stdin.readline().rstrip())


def dfs(x):
    ret = 0
    if int(x) > N:
        return ret
    if '7' in x and '5' in x and '3' in x:
        ret += 1
    for k in '753':
        ret += dfs(x + k)
    return ret


# print(dfs('0'))

# ABC119 C - Synthetic Kadomatsu
N, A, B, C = [int(x) for x in stdin.readline().rstrip().split()]
l = [int(stdin.readline().rstrip()) for _ in range(N)]


def solve(m, a, b, c):
    if m == N:
        if a == 0 or b == 0 or c == 0:
            return 10 ** 7
        else:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
    return min(solve(m + 1, a, b, c), solve(m + 1, a + l[m], b, c) + 10,
               solve(m + 1, a, b + l[m], c) + 10, solve(m + 1, a, b, c + l[m]) + 10)


print(solve(0, 0, 0, 0))
