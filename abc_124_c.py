from sys import stdin

S = stdin.readline().rstrip()
T1 = [k % 2 for k in range(len(S))]
T2 = [1 - k % 2 for k in range(len(S))]
c1 = 0
c2 = 0
for l in range(len(S)):
    if int(S[l]) == T1[l]:
        c1 += 1
    else:
        c2 += 1

print(min(c1, c2))
