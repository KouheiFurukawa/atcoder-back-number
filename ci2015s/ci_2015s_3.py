S = open('../sample.txt').readlines()

S = [s.replace('\n', '') for s in S]
printed = []

for n in range(len(S) - 1):
    if S[n] == S[n + 1] and S[n] not in printed:
        printed.append(S[n])

for x in printed:
    print(x)
