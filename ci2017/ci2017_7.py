from sys import stdin
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


def calc(x):
    if s < x:
        return 2 * x * m * m * (n // x)
    elif x <= s < 2 * x - 1:
        return 2 * n * (m ** 2)
    elif 2 * x - 1 <= s < x * m * 2:
        return x * (m + 1) * m * (n // x)
    else:
        return 2 * x * m * (n // x)


ans = (10 ** 8, 0)
X.sort()
print(X)
for k in X:
    print(calc(k))
    if calc(k) <= ans[0]:
        ans = (calc(k), k)

print(ans[1])
