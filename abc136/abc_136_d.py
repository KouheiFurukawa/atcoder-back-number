from sys import stdin

S = stdin.readline().rstrip()

A = []
r_count = 0
l_count = 0
rl = 0
ans = [0] * len(S)

for i in range(len(S)):
    if i > 0:
        if S[i] == 'L' and S[i - 1] == 'R':
            rl = i - 1
        if (S[i] == 'R' and S[i - 1] == 'L') or i == len(S) - 1:
            if i == len(S) - 1:
                l_count += 1
            A.append((r_count, l_count, rl))
            r_count = 0
            l_count = 0
            rl = 0
    if S[i] == 'R':
        r_count += 1
    if S[i] == 'L':
        l_count += 1

for a in A:
    r_index = a[2] - a[0] + 1
    l_index = a[2] + a[1]
    ans[a[2]] = (a[2] - r_index) // 2 + 1 + (l_index - a[2]) // 2
    ans[a[2] + 1] = (a[2] - r_index + 1) // 2 + 1 + (l_index - a[2] - 1) // 2

print(*ans)
