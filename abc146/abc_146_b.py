from sys import stdin

N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
ans = ''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(S)):
    j = 0
    while alphabet[j] != S[i]:
        j += 1
    ans += alphabet[(j + N) % 26]

print(ans)
