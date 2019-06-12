from sys import stdin

N, K = [int(x) for x in stdin.readline().rstrip().split()]
V_original = [int(x) for x in stdin.readline().rstrip().split()]

ans = -float('inf')  # 初期値は負の無限大！！

for i in range(K+1):  # 取り出す回数
    if i > N:
        break

    for j in range(i+1):  # 左側から取り出す回数
        V = V_original[:]
        get = []
        for k in range(j):
            get.append(V.pop(0))  # 左側から取り出す
        for k in range(i-j):
            get.append(V.pop(-1))  # 右側から取り出す

        get = sorted(get)

        for k in range(K-i):
            if len(get) > 0:
                if get[0] < 0:
                    get.pop(0)  # 負の価値の宝石は捨てる
                else:
                    break
            else:
                break

        ans = max([ans, sum(get)])

print(ans)
