from sys import stdin
import fractions
N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
ans = A[0]
for k in range(N)[1:]:
    ans = fractions.gcd(ans, A[k])
print(ans)
