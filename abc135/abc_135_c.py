from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]
cnt = 0

for i in range(N):
    kill = min(A[i], B[i])
    A[i] -= kill
    cnt += kill
    B[i] -= kill
    kill2 = min(A[i + 1], B[i])
    A[i + 1] -= kill2
    cnt += kill2

print(cnt)
