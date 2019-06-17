from sys import stdin

W, H, x, y = [int(x) for x in stdin.readline().rstrip().split()]
if W / 2 == x and H / 2 == y:
    print((W * H) / 2, 1)
else:
    print((W * H) / 2, 0)
