from sys import stdin

s = stdin.readline().rstrip()
rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

ans = 0
cnt = 0
while cnt < len(s):
    if cnt < len(s) - 1:
        if s[cnt] == 'I' and (s[cnt + 1] == 'X' or s[cnt + 1] == 'V'):
            ans += rom[s[cnt + 1]] - 1
            cnt += 2
        elif s[cnt] == 'X' and (s[cnt + 1] == 'L' or s[cnt + 1] == 'C'):
            ans += rom[s[cnt + 1]] - 10
            cnt += 2
        elif s[cnt] == 'C' and (s[cnt + 1] == 'D' or s[cnt + 1] == 'M'):
            ans += rom[s[cnt + 1]] - 100
            cnt += 2
        else:
            ans += rom[s[cnt]]
        cnt += 1
    else:
        ans += rom[s[cnt]]
        cnt += 1

print(ans)
