from sys import stdin
import fractions

N, X = [int(k) for k in stdin.readline().rstrip().split()]
x = [int(k) for k in stdin.readline().rstrip().split()]
y = [abs(k - X) for k in x]
C = y[0]
for l in range(N):
    C = fractions.gcd(C, y[l])
print(C)
