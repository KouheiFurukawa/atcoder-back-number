from sys import stdin

s = stdin.readline().rstrip()
a = 0
cnt = 0
s = s.replace('BC', '*')

print(s)
for k in s:
    if k != 'A' and k != '*':
        a = 0
    elif k == 'A':
        a += 1
    elif k == '*':
        print(a, k)
        cnt += a

print(cnt)
