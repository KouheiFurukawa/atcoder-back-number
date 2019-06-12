from sys import stdin

R = int(stdin.readline().rstrip())

if R < 1200:
    print('ABC')
elif R < 2800:
    print('ARC')
else:
    print('AGC')
