N = int(input())
# -2乗の計算
if N == 0:
    print(0)
else:
    li = []
    ind = 0
    while N != 0:
        if N % 2 ** (ind + 1) == 0:
            li.insert(0, 0)
            ind += 1
        else:
            li.insert(0, 1)
            N -= (-2) ** ind
            ind += 1
        print(N, ind, li)
    x = ''.join([str(li[i]) for i in range(len(li))])
    print(x)
