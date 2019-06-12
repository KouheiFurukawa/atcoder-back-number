from sys import stdin
import collections
S = stdin.readline().rstrip()
co = collections.Counter(S)
if len(co.most_common()) == 1:
    print('0')
else:
    print(co.most_common()[1][1] * 2)
