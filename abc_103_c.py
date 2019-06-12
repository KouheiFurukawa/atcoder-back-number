from sys import stdin
import fractions

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

lcm_a = A[0] * A[1] // fractions.gcd(A[0], A[1])

if len(A) > 2:
    for k in A[2:]:
        lcm_a = lcm_a * k // fractions.gcd(lcm_a, k)

modulo_sum = 0

for k in A:
    modulo_sum += (lcm_a - 1) % k

print(modulo_sum)
