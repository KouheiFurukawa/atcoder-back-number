data1 = open('mat1.txt').readlines()[0].split()
data2 = open('mat2.txt').readlines()[0].split()


def process(data):
    processed_data = []
    row = []
    for d in data:
        if ',' in d:
            row.append(int(d[:d.index(',')]))
            processed_data.append(row)
            row = [int(d[d.index(',') + 1:])]
        elif '.' in d:
            row.append(int(d.replace('.', '')))
            processed_data.append(row)
        else:
            row.append(int(d))
    return processed_data


pdata1 = process(data1)
pdata2 = process(data2)

ans = 0
for k in range(len(pdata1)):
    for l in range(len(pdata1[0])):
        ans += pdata1[k][l] * pdata2[l][k]

print(ans)
