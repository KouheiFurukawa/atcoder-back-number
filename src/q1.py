import numpy as np
import codecs


def q1(args):
    x, y, d = args
    if type(x) is not int or type(y) is not int or type(d) is not int:
        raise ValueError
    cnt = 0
    for i in range(2 ** 9):
        s = format(i, '09b')
        t = np.array([x if s[i] == '1' else y for i in range(9)]).reshape(3, 3)
        if int(np.linalg.det(t)) == d:
            cnt += 1
    return cnt


if __name__ == '__main__':
    A = [[int(x) for x in y.rstrip().split()] for y in open('q1_in.txt').readlines()]
    ans = []

    for a in A:
        ans.append(q1(a))

    print(*ans, sep="\n", file=codecs.open('q1_out.txt', 'w', 'utf-8'))
