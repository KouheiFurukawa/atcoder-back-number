from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
S = stdin.readline().rstrip()
cnt = 1
run = []
if len(S) == 1:
    run.append(1)
else:
    for i in range(1, len(S)):
        if S[i - 1] == S[i]:
            cnt += 1
        else:
            run.append(cnt)
            cnt = 1
        if i == len(S) - 1:
            run.append(cnt)
if S[0] == '0':
    run = [0] + run
if S[N - 1] == '0':
    run = run + [0]
if len(run) < 2 * K + 1:
    print(sum(run))
    exit()
ans = sum(run[0: 2 * K + 1])
sb = ans
for j in range(2, len(run) - 2 * K):
    if j % 2 == 1:
        continue
    else:
        sb = sb - run[j - 1] - run[j - 2] + run[j + 2 * K] + run[j + 2 * K - 1]
        if sb > ans:
            ans = sb
print(ans)
