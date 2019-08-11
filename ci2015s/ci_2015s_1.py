S = open('../sample.txt').readlines()

S = [s.replace('\n', '') for s in S]

cnt = 0
for s in S:
    for t in s:
        if t == ';':
            cnt += 1

print(cnt)