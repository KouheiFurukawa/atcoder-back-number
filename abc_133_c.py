from sys import stdin

L, R = [int(x) for x in stdin.readline().rstrip().split()]

A = [(L + x) % 2019 for x in range(min(2019, R - L + 1))]
A.sort()

ans = 10 ** 8
for l in range(len(A) - 1):
    for m in range(l + 1, len(A)):
        if (A[l] * A[m]) % 2019 < ans:
            ans = (A[l] * A[m]) % 2019

print(ans)
