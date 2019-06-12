from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
cnt = 0

for k in A:
    while k % 2 == 0:
        k /= 2
        cnt += 1

print(cnt)
