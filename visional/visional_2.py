from sys import stdin

A = [x for x in stdin.readline().rstrip().split(' ')]
m = int(A[-1])
N = []

for i in range(len(A) - 1):
    S = A[i].split(':')
    N.append((int(S[0]), S[1]))

N.sort(key=lambda x: x[0])
ans = ''

for i in range(len(N)):
    if m % N[i][0] == 0:
        ans = ans + N[i][1]

if ans == '':
    print(m)
else:
    print(ans)
