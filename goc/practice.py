from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline().rstrip())

    for i in range(n):
        print('Case #{}:'.format(i + 1))
        d = {}
        m = int(stdin.readline().rstrip())
        for j in range(m):
            name, price = stdin.readline().rstrip().split()
            if name not in d:
                d[name] = (1, int(price), int(price), int(price))
            else:
                d[name] = (d[name][0] + 1, min(d[name][1], int(price)), max(d[name][2], int(price)), int(price) + d[name][3])
        for k in d:
            print(k, k.value[0])
