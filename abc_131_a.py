from sys import stdin, exit

S = stdin.readline().rstrip()

for k in range(len(S) - 1):
    if S[k] == S[k + 1]:
        print('Bad')
        exit()
print('Good')
