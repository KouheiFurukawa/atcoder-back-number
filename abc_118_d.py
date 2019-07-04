from sys import stdin

N, M = [int(x) for x in stdin.readline().rstrip().split()]
S = [2, 5, 5, 4, 5, 6, 3, 7, 6]
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [(x, S[x - 1]) for x in A]
B.sort(key=lambda x: x[1])
numbers = ''


def digits(match, ans):
    global numbers
    if match == 0:
        return len(ans), ans
    if match < B[0][1]:
        return -1, ''
    return sorted([digits(match - B[k][1], ans + str(B[k][0])) for k in range(len(A))], key=lambda x: x[0], reverse=True)[0]


print(sorted(digits(N, '')[1], reverse=True))
