from sys import stdin

N = int(stdin.readline().rstrip())
W = [int(x) for x in stdin.readline().rstrip().split()]
ans = 10 ** 7
for i in range(N):
    ans = min(ans, abs(sum(W[:i + 1]) - sum(W[i + 1:])))
print(ans)
