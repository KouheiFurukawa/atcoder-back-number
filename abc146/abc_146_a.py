from sys import stdin

S = stdin.readline().rstrip()

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(7 - days.index(S))
