from sys import stdin, exit

S = int(stdin.readline().rstrip())
if S == 10 ** 18:
    print(0, 0, 10 ** 9, 0, 0, 10 ** 9)
    exit()
else:
    a = 10 ** 9
    b = 1
    c = 10 ** 9 - S % (10 ** 9)
    d = S // (10 ** 9) + 1
    print(0, 0, a, b, c, d)
