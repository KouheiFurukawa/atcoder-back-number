S = open('../sample.txt').readlines()
S = [s.replace('\n', '') for s in S]

for i in range(len(S)):
    print(i + 1, S[i])
