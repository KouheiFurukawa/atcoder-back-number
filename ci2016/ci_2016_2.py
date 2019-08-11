from sys import stdin

data = [[x for x in stdin.readline().rstrip()] for _ in range(5)]
scan = ['' for x in range(len(data[0]))]
for k in range(len(data)):
    for l in range(len(data[k])):
        scan[l] += data[k][l]

result = ''
cnt = 0
print(scan)
while cnt < len(scan):
    if scan[cnt] == '*    ':
        result += '7'
        cnt += 6
        continue
    elif scan[cnt] == '*|* *':
        result += '5'
        cnt += 6
        continue
    elif scan[cnt] == '* *|*':
        result += '2'
        cnt += 6
        continue
    elif scan[cnt] == '* * *':
        result += '3'
        cnt += 6
        continue
    elif scan[cnt] == '*|*  ':
        if scan[cnt + 1] == '* *  ':
            result += '9'
            cnt += 6
            continue
        if scan[cnt + 1] == '  *  ':
            result += '4'
            cnt += 6
            continue
    elif scan[cnt] == '*|*|*':
        if scan[cnt + 1] == '*   *':
            result += '0'
            cnt += 6
            continue
        if scan[cnt + 1] == '     ':
            result += '1'
            cnt += 3
            continue
        if scan[cnt + 1] == '  * *':
            result += '6'
            cnt += 6
            continue
        if scan[cnt + 1] == '* * *':
            result += '8'
            cnt += 6
            continue

print(result)
