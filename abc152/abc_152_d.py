from sys import stdin

N = int(stdin.readline().rstrip())
ans = 0
d = 0
M = [[0] * 10 for _ in range(10)]

for i in range(1, N + 1):
    s = str(i)
    M[int(s[0])][int(s[-1])] += 1

for i in range(10):
    for j in range(10):
        if i == j:
            d += M[i][j] * M[j][i]
        else:
            ans += M[i][j] * M[j][i]

print(ans + d)
