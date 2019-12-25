from sys import stdin

S = stdin.readline().rstrip()

ans = [-1] * (len(S) + 1)
for i in range(len(S)):
    if i == 0 and S[i] == '<':
        ans[i] = 0
    if i > 0 and S[i - 1] == '>' and S[i] == '<':
        ans[i] = 0
if S[-1] == '>':
    ans[len(S)] = 0

for i in range(len(S) + 1):
    if ans[i] == 0:
        cnt = 0
        while i + cnt <= len(S) - 1 and S[i + cnt] == '<' and ans[i + cnt + 1] != 0:
            ans[i + cnt + 1] = max(ans[i + cnt + 1], ans[i + cnt] + 1)
            # print(ans)
            cnt += 1
        cnt = 0
        while i + cnt >= 0 and S[i + cnt - 1] == '>' and ans[i + cnt - 1] != 0:
            ans[i + cnt - 1] = max(ans[i + cnt - 1], ans[i + cnt] + 1)
            # print(ans)
            cnt -= 1

# print(ans)
print(sum(ans))
