n = 2


def calc(d):
    return d * d * (3 ** 0.5) / 4


e = 3
el = 10
x = 0
s = calc(el)

while x < n:
    x += 1
    el /= 3
    s += e * calc(el)
    e = 4 * e

print(s)
