from sympy import *

x = Symbol('x')

b = solve((2811.88 * x + 1774.42) * 2399360 / 2811.88 * x ** (-9 / 7) - 2734.62 - 8397760 * (1 - x ** (-2 / 7)), x)

print(2399360 / 2811.88 * b[0] ** (-9 / 7))

print(2399360 / 2811.88)
