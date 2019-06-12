from sys import stdin
s = int(stdin.readline().rstrip())
A = []
while True:
    if s not in A:
        A.append(s)
    else:
        break
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
print(len(A) + 1)
