from sys import stdin

N = int(stdin.readline().rstrip())
ans = 10 ** 13
A = 1
while A ** 2 <= N:
    if N % A == 0:
        if A + (N // A) < ans:
            ans = A + (N // A)
    A += 1
print(ans - 2)
