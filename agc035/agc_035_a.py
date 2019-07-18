from sys import stdin, exit

N = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split()]

num = []
count = []
for k in a:
    if k not in num:
        num.append(k)
        count.append(1)
    else:
        count[num.index(k)] += 1
    if len(num) > 3:
        print('No')
        exit()
if len(num) == 1 and num[0] == 0:
    print('Yes')
    exit()
if len(num) == 2 and num[0] ^ num[1] == num[1] and N % 3 == 0 and count[1] == 2 * count[0]:
    print('Yes')
    exit()
if len(num) == 2 and num[0] ^ num[1] == num[0] and N % 3 == 0 and count[0] == 2 * count[1]:
    print('Yes')
    exit()
if len(num) <= 2:
    print('No')
    exit()
if (num[0] ^ num[1] == num[2] or num[0] ^ num[2] == num[1] or num[1] ^ num[1] == num[0]) and N % 3 == 0 and count[0] == count[1] == count[2]:
    print('Yes')
else:
    print('No')
