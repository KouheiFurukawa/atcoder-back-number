from sys import stdin

N = int(stdin.readline().rstrip())
p = [int(x) for x in stdin.readline().rstrip().split()]

cnt = 0
for k in range(len(p)):
    if p[k] != k + 1:
        cnt += 1

if cnt == 2 or cnt == 0:
    print('YES')
else:
    print('NO')
