from sys import stdin
import collections
n = int(stdin.readline().rstrip())
V = [int(x) for x in stdin.readline().rstrip().split()]
V_odd = [V[2 * k] for k in range(int(n / 2))]
V_even = [V[2 * k + 1] for k in range(int(n / 2))]
co = collections.Counter(V_odd)
ce = collections.Counter(V_even)
if co.most_common()[0][0] != ce.most_common()[0][0]:
    print(n - co.most_common()[0][1] - ce.most_common()[0][1])
elif len(co.most_common()) == 1 and len(ce.most_common()) == 1:
    print(co.most_common()[0][1])
else:
    print(n - (max(co.most_common()[1][1] + ce.most_common()[0][1], co.most_common()[0][1] + ce.most_common()[1][1])))
