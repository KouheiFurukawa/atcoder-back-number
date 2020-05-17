def insertion_sort(a):
    for i in range(1, len(a)):
        j = i - 1
        temp = a[i]
        while a[j] > temp and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    return a


def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


def bubble_sort(a):
    for i in range(len(a)):
        j = len(a) - 1
        while j > i:
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) == 0:
            result.append(right.pop())
            continue
        if len(right) == 0:
            result.append(left.pop())
            continue
        if left[0] > right[0]:
            result.append(right[0])
            right = right[1:]
            continue
        else:
            result.append(left[0])
            left = left[1:]
            continue
    return result


def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = []
    right = []
    pivot_cnt = 1
    for i in range(1, len(a)):
        if a[i] < pivot:
            left.append(a[i])
        elif a[i] > pivot:
            right.append(a[i])
        else:
            pivot_cnt += 1
    return quick_sort(left) + [pivot] * pivot_cnt + quick_sort(right)


def count_sort(a):
    if len(a) <= 1:
        return a
    max_a = 0
    for i in range(len(a)):
        max_a = max(a[i], max_a)
    c = [0] * (max_a + 1)
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(max_a):
        c[i + 1] += c[i]
    ans = [0] * len(a)
    index = len(a) - 1
    while index >= 0:
        ans[c[a[index]] - 1] = a[index]
        c[a[index]] -= 1
        index -= 1
    return ans


if __name__ == '__main__':
    arr = [5, 1, 4, 7, 2, 100, 3, 35, 21, 565]
    # print(insertion_sort(arr))
    # print(selection_sort(arr))
    # print(bubble_sort(arr))
    # print(merge_sort(arr))
    # print(quick_sort(arr))
    print(count_sort(arr))

