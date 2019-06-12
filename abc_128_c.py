from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
KS = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(M)]
p = [int(x) for x in stdin.readline().rstrip().split()]

k = [KS[l][0] for l in range(M)]
s = [KS[m][1:] for m in range(M)]
cnt = 0


def to_binary(x):
    out = ''
    for l in range(N):
        if x >= 2 ** (N - l - 1):
            out += '1'
            x -= 2 ** (N - l - 1)
        else:
            out += '0'
    return out


for m in range(2 ** N):
    bin_num = to_binary(m)
    for x in range(M):
        swi = 0
        for y in range(k[x]):
            if bin_num[s[x][y] - 1] == '1':
                swi += 1
        if swi % 2 != p[x]:
            break
        if x == M - 1:
            cnt += 1

print(cnt)

