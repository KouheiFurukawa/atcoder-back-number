from sys import stdin

data = stdin.readline().rstrip().split()
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

print(len(processed_data), len(processed_data[0]))
