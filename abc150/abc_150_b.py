from sys import stdin

N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
ans = 0

for i in range(N - 2):
    if S[i] == 'A' and S[i + 1] == 'B' and S[i + 2] == 'C':
        ans += 1

print(ans)
