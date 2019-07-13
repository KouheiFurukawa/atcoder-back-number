from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

S = sum(A)
ans = [0 for _ in range(N)]
s = 0
for k in range(int((N - 1) / 2)):
    s += A[2 * k + 1] * 2
ans[0] = S - s
for k in range(1, N):
    ans[k] = A[k - 1] * 2 - ans[k - 1]
print(*ans)
