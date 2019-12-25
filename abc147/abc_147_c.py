from sys import stdin

N = int(stdin.readline().rstrip())
wit = [[] for _ in range(N)]
A = []

for i in range(N):
    A = int(stdin.readline().rstrip())
    for n in range(A):
        wit[i].append([int(x) for x in stdin.readline().rstrip().split()])

ans = 0

for i in range(2 ** N):
    s = bin(i)[2:].zfill(N)
    one_cnt = 0
    tmp = 0
    for j in range(N):
        if s[j] == '1':
            one_cnt += 1
            cnt = 0
            for k in wit[j]:
                if k[1] == 1:
                    if s[k[0] - 1] == '1':
                        cnt += 1
                elif k[1] == 0:
                    if s[k[0] - 1] == '0':
                        cnt += 1
            if cnt == len(wit[j]):
                tmp += 1
    if tmp == one_cnt:
        ans = max(ans, one_cnt)

print(ans)
