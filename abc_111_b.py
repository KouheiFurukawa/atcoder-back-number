from sys import stdin
N = stdin.readline().rstrip()
if int(N) > int(N[0] * 3):
    print(str(int(N[0]) + 1) * 3)
else:
    print(N[0] * 3)
