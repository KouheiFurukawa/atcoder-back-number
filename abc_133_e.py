from sys import stdin


def LI(): return list(map(int, stdin.readline().split()))


inf = 1000000007


def main():
    N, K = LI()
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = LI()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    stack = [0]
    ans = 1
    done = [False] * N
    while len(stack) > 0:
        now = stack.pop()
        done[now] = True
        cnt = 0
        for x in graph[now]:
            if not done[x]:
                cnt += 1
                stack.append(x)
        if now == 0:
            for i in range(cnt):
                ans = (K - 1 - i) * ans % inf
        else:
            for i in range(cnt):
                ans = (K - 2 - i) * ans % inf
    print(ans * K % inf)


if __name__ == "__main__":
    main()
