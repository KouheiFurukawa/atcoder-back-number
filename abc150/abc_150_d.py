from sys import stdin
import fractions

N, M = [int(x) for x in stdin.readline().rstrip().split()]
A = [int(x) // 2 for x in stdin.readline().rstrip().split()]
ans = 0
g = 1

for i in range(len(A)):
    g = g * A[i] // fractions.gcd(g % A[i], A[i])
    if g > M:
        print(0)
        exit()

for i in range(len(A)):
    if (g // A[i]) % 2 == 0:
        print(0)
        exit()

ans = M // g
if ans % 2 == 0:
    print(ans // 2)
else:
    print((ans + 1) // 2)
