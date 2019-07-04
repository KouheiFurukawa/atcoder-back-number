from sys import stdin
import fractions

A, B, C, D = [int(x) for x in stdin.readline().rstrip().split()]


def div(n, x, y):
    lcs = int(x * y / fractions.gcd(x, y))
    return n - int(n // x) - int(n // y) + int(n // lcs)


print(div(B, C, D) - div(A - 1, C, D))
