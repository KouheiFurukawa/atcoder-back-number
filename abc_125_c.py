from sys import stdin
import fractions

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
L = [0]*(N+2)
R = [0]*(N+2)
ans = 0
for i in range(N):
    L[i+1] = (fractions.gcd(L[i],A[i]))
    R[N-i] = (fractions.gcd(R[N-i+1],A[N-1-i]))
print(L, R)
for i in range(N):
    ans = max(ans,(fractions.gcd(L[i], R[i+2])))
print(ans)
