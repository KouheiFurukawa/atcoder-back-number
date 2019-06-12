from sys import stdin

N = int(stdin.readline().rstrip())
W = []
for k in range(N):
    w = stdin.readline().rstrip()
    if k >= 1:
        if w[0] != W[k - 1][len(W[k - 1]) - 1] or len([x for x in W if x == w]) > 0:
            print('No')
            break
    W.append(w)
if len(W) == N:
    print('Yes')
