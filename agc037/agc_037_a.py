from sys import stdin

S = stdin.readline().rstrip()
cnt = 0

before = ''
test = ''
for i in range(len(S)):
    test += S[i]
    if test != before:
        cnt += 1
        before = test
        test = ''
    else:
        continue

print(cnt)
