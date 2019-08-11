S = [s.replace('\n', '') for s in open('../sample.txt').readlines()]
all_ans = []

i = 0
while i < len(S):
    ans = []
    for j in range(i):
        if S[i] == S[j]:
            cnt = 1
            n_ans = [S[j]]
            while i + cnt < len(S) and S[i + cnt] == S[j + cnt] and j + cnt < i:
                n_ans.append(S[j + cnt])
                cnt += 1
            if cnt >= 4:
                if len(ans) < len(n_ans):
                    ans = n_ans
    if len(ans) > 0:
        if ans not in all_ans:
            all_ans.append(ans)
        i += len(ans)
        if i >= len(S):
            break
        continue
    i += 1

for ans in all_ans:
    for a in ans:
        print(a)
    print(' ')
