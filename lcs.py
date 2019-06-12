from sys import stdin

X = stdin.readline().rstrip()
Y = stdin.readline().rstrip()

m = len(X)
n = len(Y)
c = [[0] * (n + 1) for x in range(m + 1)]
maxl = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        print(i, j)
        if X[i - 1] == Y[j - 1]:
            c[i][j] = c[i - 1][j - 1] + 1
        elif c[i - 1][j] >= c[i][j - 1]:
            c[i][j] = c[i - 1][j]
        else:
            c[i][j] = c[i][j - 1]
        maxl = max(maxl, c[i][j])

print(*c, sep='\n')
print(maxl)
