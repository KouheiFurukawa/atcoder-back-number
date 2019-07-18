from sys import stdin
import bisect

s = stdin.readline().rstrip()
rom = [1, 5, 10, 50, 100, 500, 1000]
a = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
ans = ''

while int(s) > 0:
    num = int(s[0]) * (10 ** (len(s) - 1))
    if num == 9:
        ans += 'IX'
        s = str(int(s) - 9)
        continue
    if num == 90:
        ans += 'XC'
        s = str(int(s) - 90)
        continue
    if num == 900:
        ans += 'CM'
        s = str(int(s) - 900)
        continue
    if num == 4:
        ans += 'XC'
        s = str(int(s) - 4)
        continue
    if num == 40:
        ans += 'XL'
        s = str(int(s) - 40)
        continue
    if num == 400:
        ans += 'CD'
        s = str(int(s) - 400)
        continue
    bi = bisect.bisect_right(rom, num) - 1
    ans += a[bi] * (num // rom[bi])
    s = str(int(s) - rom[bi] * (num // rom[bi]))

print(ans)
