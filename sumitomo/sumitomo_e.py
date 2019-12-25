from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
inf = 1000000007

ans = 1
cap = [0, 0, 0]
for i in range(N):
    tmp = 0
    for j in range(3):
        if cap[j] == A[i]:
            tmp += 1
    for j in range(3):
        if cap[j] == A[i]:
            cap[j] += 1
            break
    ans *= tmp
    ans %= inf

print(ans)
