S = [s.replace('\n', '') for s in open('../sample.txt').readlines()]
ans_cnt = 0


def compare(s, t):
    global ans_cnt
    if len(s) < 20 or len(t) < 20:
        return
    if len(s) < len(t):
        s = s + ' ' * (len(t) - len(s))
    elif len(s) > len(t):
        t = t + ' ' * (len(s) - len(t))
    cnt = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            cnt += 1
    if cnt >= 5:
        return
    else:
        print(s)
        print(t)
        ans_cnt += 1


for j in range(len(S) - 1):
    for k in range(j + 1, len(S)):
        compare(S[j], S[k])

print(ans_cnt)