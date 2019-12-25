from sys import stdin
import math

a, b, x = [int(x) for x in stdin.readline().rstrip().split()]

if x == (a ** 2) * b:
    print(0)
    exit()
if 2 * x >= (a ** 2) * b:
    v = (a ** 2) * b - x
    c = (2 * v) / (a ** 2)
    print(90 - math.atan(a / c) * 180 / math.pi)
else:
    c = 2 * x / (a * b)
    print(math.atan(b / c) * 180 / math.pi)
