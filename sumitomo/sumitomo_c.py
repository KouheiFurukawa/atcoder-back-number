from sys import stdin

X = int(stdin.readline().rstrip())

if X < 100:
    print(0)
    exit()
num = X // 100
s = X % 100
if s > 5 * num and X < 2000:
    print(0)
else:
    print(1)
