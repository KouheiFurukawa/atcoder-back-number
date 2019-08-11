from sys import stdin, exit

N = int(stdin.readline().rstrip())
H = [int(x) for x in stdin.readline().rstrip().split()]
drop = 0

if N == 1:
    print('Yes')
    exit()

if N == 2:
    if H[0] - H[1] > 1:
        print('No')
        exit()
    else:
        print('Yes')
        exit()

for i in range(N - 2, -1, -1):
    if H[i] - H[i + 1] > 1:
        print('No')
        exit()
    if H[i] - H[i + 1] == 1:
        H[i] -= 1
print('Yes')
