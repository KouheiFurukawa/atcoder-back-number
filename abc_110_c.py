from sys import stdin

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cnt = 0

for letter in alphabet:
    X = []
    Y = []
    for k in range(len(T)):
        if T[k] == letter:
            X.append(S[k])
            if len(X) > 1 and X[len(X) - 1] != X[len(X) - 2]:
                print('No')
                break
        if S[k] == letter:
            Y.append(T[k])
            if len(Y) > 1 and Y[len(Y) - 1] != Y[len(Y) - 2]:
                print('No')
                break
    if len(X) > 1 and X[len(X) - 1] != X[len(X) - 2]:
        break
    if len(Y) > 1 and Y[len(Y) - 1] != Y[len(Y) - 2]:
        break
    cnt += 1

if cnt == 26:
    print('Yes')
