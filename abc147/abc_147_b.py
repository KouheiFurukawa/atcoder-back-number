from sys import stdin

S = stdin.readline().rstrip()
c = len(S) // 2
ans = 0

for i in range(c):
    if S[i] != S[len(S) - i - 1]:
        ans += 1

print(ans)
