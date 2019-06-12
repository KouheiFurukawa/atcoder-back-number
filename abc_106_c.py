from sys import stdin

S = stdin.readline().rstrip()
K = int(stdin.readline().rstrip())

for x in range(len(S)):
    if int(S[x]) > 1:
        print(S[x])
        break
    if K == x + 1:
        print('1')
        break
