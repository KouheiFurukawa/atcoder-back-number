from sys import stdin
import sys
sys.setrecursionlimit(10000)

n = int(stdin.readline().rstrip())
flowers = [int(x) for x in stdin.readline().rstrip().split()]


def watering(s, count):
    index_fwd = 10 ** 9
    index_back = 0
    for k in range(len(s)):
        if s[k] > 0:
            index_fwd = k
            break
    if index_fwd == 10 ** 9:
        return count
    for l in range(index_fwd, len(s)):
        if s[l] == 0:
            break
        index_back = l
    for m in range(index_fwd, index_back + 1):
        s[m] -= 1
    count += 1
    return watering(s, count)


print(watering(flowers, 0))
