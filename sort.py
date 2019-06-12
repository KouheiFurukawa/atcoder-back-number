from sys import stdin

N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]


def insertion_sort(a, n):
    for k in range(n):
        v = a[k]
        j = k - 1
        while (j >= 0) & (a[j] > v):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v
    return a


def bubble_sort(a, n):
    flag = 1
    while flag == 1:
        flag = 0
        for j in range(1, n)[::-1]:
            if a[j] < a[j - 1]:
                v = a[j]
                a[j] = a[j - 1]
                a[j - 1] = v
                flag = 1
    return a


def selection_sort(a, n):
    for k in range(n):
        v = k
        for l in range(k + 1, n):
            if a[l] < a[v]:
                v = l
        w = a[k]
        a[k] = a[v]
        a[v] = w
    return a


print(bubble_sort(A, N))
