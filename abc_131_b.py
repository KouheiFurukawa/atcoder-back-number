from sys import stdin

N, L = [int(x) for x in stdin.readline().rstrip().split()]

apples = [L + i for i in range(N)]
apples_minus = sorted([x for x in apples if x <= 0], reverse=True)
apples_minus.append(-10 ** 8)
apples_plus = sorted([x for x in apples if x >= 0])
apples_plus.append(10 ** 8)
eat = 0
if abs(apples_minus[0]) <= abs(apples_plus[0]):
    eat = apples_minus[0]
else:
    eat = apples_plus[0]
print(sum(apples) - eat)
