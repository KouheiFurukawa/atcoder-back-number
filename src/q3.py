import heapq
import codecs

# 間隙に座った時にできる新しい間隙のうち短い方の長さを返す
def get_next_gap(n):
    return -((n - 1) // 2)

def q3(args):
    n, a1 = args
    if a1 > n:
        raise ValueError
    # 一人目が座った後の間隙を記録、キーは「その間隙に人が座った時にできる間隙の長さ」
    q = []
    if a1 >= 2:
        q.append((2 - a1, 0, a1 - 1))
    if a1 <= n - 1:
        q.append((a1 + 1 - n, a1, n))
    heapq.heapify(q)
    # 出力
    out = 0
    # 偶奇判定用のカウント
    cnt = 1

    # 最大の間隙を選んで座る
    while len(q) > 0:
        g = heapq.heappop(q)
        if g[1] == g[2]:
            break

        cnt += 1
        # 左端
        if g[1] == 0:
            if g[2] - 1 > 0:
                h = (get_next_gap(g[2] - 1), 1, g[2])
                heapq.heappush(q, h)
            if cnt % 2 == 0:
                out += 1
            continue
        # 右端
        elif g[2] == args[0]:
            if g[2] - 1 - g[1] >= 1:
                h = (get_next_gap(g[2] - 1 - g[1]), g[1], g[2] - 1)
                heapq.heappush(q, h)
            if cnt % 2 == 0:
                out += g[2]
            continue
        else:
            left_gap = -g[0]
            right_gap = g[2] - g[1] - 1 - left_gap
            if left_gap >= 1:
                h1 = (get_next_gap(left_gap), g[1], g[1] + left_gap)
                heapq.heappush(q, h1)
            if right_gap >= 1:
                h2 = (get_next_gap(right_gap), g[2] - right_gap, g[2])
                heapq.heappush(q, h2)
            if cnt % 2 == 0:
                out += g[1] + left_gap + 1

    return out


if __name__ == '__main__':
    A = [[int(x) for x in y.rstrip().split()] for y in open('q3_in.txt').readlines()]
    ans = []

    for a in A:
        ans.append(q3(a))

    print(*ans, sep="\n", file=codecs.open('q3_out.txt', 'w', 'utf-8'))
