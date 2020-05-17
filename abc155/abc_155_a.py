from sys import stdin

A, B, C = stdin.readline().rstrip().split()

if A == B and A != C:
    print('Yes')
    exit()

if A == C and A != B:
    print('Yes')
    exit()

if B == C and A != C:
    print('Yes')
    exit()

print('No')
