from sys import stdin

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()

for k in range(len(S)):
    if S[k:] + S[:k] == T:
        print('Yes')
        break
    if k == len(S) - 1:
        print('No')
