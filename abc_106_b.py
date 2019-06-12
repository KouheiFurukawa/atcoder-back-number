from sys import stdin

N = int(stdin.readline().rstrip())

sosuu = [3, 5, 7, 11, 13]

if N < 105:
    print('0')
elif N < 135:
    print('1')
elif N < 165:
    print('2')
elif N < 189:
    print('3')
elif N < 195:
    print('4')
else:
    print('5')
