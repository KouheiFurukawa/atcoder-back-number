from sys import stdin

K = int(stdin.readline().rstrip())
X, Y = [int(x) for x in stdin.readline().rstrip().split()]


def solve(m, n):
    x = abs(m)
    y = abs(n)
    res = (22 - x - y) // 2
    if x < y:
        output = [[x + res, K - (x + res)], [-res, y - K + (x + res)]]
    else:
        output = [[K - (y + res), y + res], [x - K + (y + res), -res]]
    if m < 0:
        output = [[-o[0], o[1]] for o in output]
    if n < 0:
        output = [[o[0], -o[1]] for o in output]
    return output


ans = []
xs = X // K
ys = Y // K

if X < 0:
    ans.extend([[-K, 0] * xs])
else:
    ans.extend([[K, 0] * xs])
if Y < 0:
    ans.extend([[0, -K] * ys])
else:
    ans.extend([[0, K] * ys])

xa = abs(X) % K
ya = abs(Y) % K

print(xa, ya)
if xa % 2 != ya % 2:
    if xa >= 0:
        ans.append([K, 0])
        xa -= K
    else:
        ans.append([-K, 0])
        xa += K

ans.extend(solve(xa, ya))

print(ans)