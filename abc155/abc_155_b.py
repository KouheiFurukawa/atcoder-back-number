from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]

for a in A:
    if a % 2 == 0 and (a % 3 != 0 and a % 5 != 0):
        print('DENIED')
        exit()

print('APPROVED')
