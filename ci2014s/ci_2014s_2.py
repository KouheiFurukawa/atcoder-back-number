from sys import stdin

d = float(stdin.readline().rstrip())
c = int(10 // d + 1)
x = c ** 2
p = 0
q = 0
y = 0
for k in range(c):
    for l in range(c):
        pp = k * d
        qq = l * d
        if (pp - 5) ** 2 + (qq - 5) ** 2 <= 25:
            y += 1

print((y / x) / 4)
