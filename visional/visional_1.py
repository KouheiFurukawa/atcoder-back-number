from sys import stdin

S = stdin.readline().rstrip()
A = []

for s in S:
    A.append(int(s))

A.sort()

ans = ''

for a in A:
    ans = ans + str(a)

if ans[0] == '0':
    index = 0
    for n in range(len(A)):
        if int(ans[n]) > 0:
            index = n
            break
    ans = ans[index] + ans[:index] + ans[index + 1:]

print(ans)
