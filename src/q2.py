import codecs

ans = []
s_len = [1, 1, 1]

s1 = 'a'
s2 = 'b'
s3 = 'c'

for i in range(30):
    s1, s2, s3 = s2, s3, s3 + s2 + s1
    l = s_len[-1] + s_len[-2] + s_len[-3]
    s_len.append(l)

def q2(args):
    k, p, q = args
    cnt = {'a': 0, 'b': 0, 'c': 0}
    if k <= 30:
        if p < 1 or q > s_len[k - 1]:
            raise ValueError
        for j in range(s_len[k - 1] - q, s_len[k -1] + 1 - p):
            cnt[s3[j]] += 1
        return 'a:{},b:{},c:{}'.format(cnt['a'], cnt['b'], cnt['c'])
    elif k > 50:
        raise ValueError


if __name__ == '__main__':
    A = [[int(x) for x in y.rstrip().split()] for y in open('q2_in.txt').readlines()]
    for a in A:
        out = q2(a)
        if out is not None:
            ans.append(out)

    print(*ans, sep="\n", file=codecs.open('q2_out.txt', 'w', 'utf-8'))
