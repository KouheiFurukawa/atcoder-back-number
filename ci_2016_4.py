from sys import stdin

data = [[x for x in stdin.readline()] for _ in range(len(open('out3.txt').readlines()))]
scan = ['' for x in range(len(data[0]))]
for k in range(len(data)):
    for l in range(len(data[k])):
        scan[l] += data[k][l]

scan_process = []
blank = 0
for s in scan[:-1]:
    index = 0
    for l in s:
        if l == ' ':
            index += 1
        else:
            blank = 0
            scan_process.append(s[index: index + 5])
            break
    if index == len(s):
        blank += 1
    if blank == 2:
        scan_process.append('     ')
        scan_process.append('     ')

result = ''
cnt = 0
print(scan_process)
while cnt < len(scan_process):
    if scan_process[cnt] == '*    ':
        result += '7'
        cnt += 6
        continue
    elif scan_process[cnt] == '*|* *':
        result += '5'
        cnt += 6
        continue
    elif scan_process[cnt] == '* *|*':
        result += '2'
        cnt += 6
        continue
    elif scan_process[cnt] == '* * *':
        result += '3'
        cnt += 6
        continue
    elif scan_process[cnt] == '*|*  ':
        if scan_process[cnt + 1] == '* *  ':
            result += '9'
            cnt += 6
            continue
        if scan_process[cnt + 1] == '  *  ':
            result += '4'
            cnt += 6
            continue
    elif scan_process[cnt] == '*|*|*':
        if scan_process[cnt + 1] == '*   *':
            result += '0'
            cnt += 6
            continue
        if scan_process[cnt + 1] == '     ':
            result += '1'
            cnt += 3
            continue
        if scan_process[cnt + 1] == '  * *':
            result += '6'
            cnt += 6
            continue
        if scan_process[cnt + 1] == '* * *':
            result += '8'
            cnt += 6
            continue

print(result)
