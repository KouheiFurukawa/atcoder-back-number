class Node:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self, data_list):
        self.data = data_list
        for i in range(len(data_list) // 2, 0, -1):
            self.max_heapify(i)


    def max_heapify(self, key):
        index = key - 1
        r = key * 2
        l = key * 2 - 1
        if r <= len(self.data) - 1 and self.data[r] > self.data[index]:
            self.data[r], self.data[index] = self.data[index], self.data[r]
            largest = r + 1
        else:
            largest = key
        if l <= len(self.data) - 1 and self.data[l] > self.data[index]:
            self.data[l], self.data[index] = self.data[index], self.data[l]
            largest = l + 1
        if largest != key:
            self.max_heapify(largest)


    def heap_extract_max(self):
        max_key = self.data[0]
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]
        self.max_heapify(1)
        return max_key


    def heap_insert(self, val):
        self.data.append(val)
        k = len(self.data)
        while k > 1 and self.data[k - 1] > self.data[k // 2 - 1]:
            self.data[k - 1], self.data[k // 2 - 1] = self.data[k // 2 - 1], self.data[k - 1]
            k //= 2


if __name__ == '__main__':
    arr = [1, 3, 6, 2, 4, 10]
    heap = MaxHeap(arr)
    heap.heap_insert(30)
    print(heap.heap_extract_max())
