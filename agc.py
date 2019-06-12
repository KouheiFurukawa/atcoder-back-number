from sys import stdin, exit

N, A, B, C, D = [int(x) for x in stdin.readline().rstrip().split()]
S = stdin.readline().rstrip()
for k in range(A - 1, max(D, C)):
    if S[k] == '#' and S[k + 1] == '#':
        print('No')
        exit()

if C < D:
    print('Yes')
else:
    cnt = 0
    for k in range(B - 2, D + 1):
        if S[k] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt > 2:
            print('Yes')
            exit()
    print('No')
