from sys import stdin
N = stdin.readline().rstrip()
S = 0
for k in N:
    S += int(k)
if int(N) % S == 0:
    print('Yes')
else:
    print('No')
