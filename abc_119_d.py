from sys import stdin
import bisect

A, B, Q = [int(x) for x in stdin.readline().rstrip().split()]
S = [int(stdin.readline().rstrip()) for _ in range(A)]
T = [int(stdin.readline().rstrip()) for _ in range(B)]
X = [int(stdin.readline().rstrip()) for _ in range(Q)]
S.append(10 ** 18)
T.append(10 ** 18)
S.insert(0, -10 ** 18)
T.insert(0, -10 ** 18)

for x in X:
    index_s = bisect.bisect_left(S, x)
    index_t = bisect.bisect_left(T, x)
    print(min(
        abs(S[index_s - 1] - T[index_t - 1]) + abs(x - S[index_s - 1]),
        abs(S[index_s - 1] - T[index_t - 1]) + abs(x - T[index_t - 1]),
        abs(S[index_s] - T[index_t - 1]) + abs(x - S[index_s]),
        abs(S[index_s] - T[index_t - 1]) + abs(x - T[index_t - 1]),
        abs(S[index_s] - T[index_t]) + abs(x - S[index_s]),
        abs(S[index_s] - T[index_t]) + abs(x - T[index_t]),
        abs(S[index_s - 1] - T[index_t]) + abs(x - S[index_s - 1]),
        abs(S[index_s - 1] - T[index_t]) + abs(x - T[index_t]),
    ))
