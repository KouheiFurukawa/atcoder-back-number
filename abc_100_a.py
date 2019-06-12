from sys import stdin

A, B = stdin.readline().rstrip().split()

if (int(A) <= 8) & (int(B) <= 8):
    print('Yay!')
else:
    print(':(')
