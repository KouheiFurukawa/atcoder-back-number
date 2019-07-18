from sys import stdin
import bisect

s = stdin.readline().rstrip()
orig = [1, 5, 10, 50, 100, 500, 1000]
rom = [1, 4, 5, 9, 10, 40, 45, 49, 50, 90, 95, 99, 100, 400, 450, 490, 495, 499, 500, 900, 950, 990, 995, 999, 1000]
a = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'VL', 'IL', 'L', 'XC', 'VC', 'IC', 'C', 'CD', 'LD', 'XD', 'VD', 'ID', 'D', 'CM',
     'LM', 'XM', 'VM', 'IM', 'M']

ans = ''

while int(s) > 0:
    num = int(s)
    bi = bisect.bisect_right(rom, num) - 1
    ans += a[bi] * (num // rom[bi])
    s = str(int(s) - rom[bi] * (num // rom[bi]))

print(ans)
