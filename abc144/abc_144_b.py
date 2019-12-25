from sys import stdin

N = int(stdin.readline().rstrip())

for j in range(1, 10):
    for k in range(1, 10):
        if j * k == N:
            print('Yes')
            exit()

print('No')
