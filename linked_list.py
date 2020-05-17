class ListItem:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, data_list):
        self.head = ListItem(None)
        self.head.prev = self.head
        self.head.next = self.head
        for d in data_list:
            self.insert(d)

    def insert(self, val):
        node = ListItem(val)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete(self, val):
        node_temp = self.head
        while node_temp.data != val:
            node_temp = node_temp.next
        node_temp.prev.next = node_temp.next
        node_temp.next.prev = node_temp.prev

    def delete_first(self):
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def delete_last(self):
        self.head.prev = self.head.prev.prev
        self.head.prev.next = self.head

    def print_content(self):
        node = self.head.next
        while node.data is not None:
            print(node.data)
            node = node.next

if __name__ == '__main__':
    ll = LinkedList([1, 5, 3, 8, 9])
    # ll.delete_first()
    ll.delete_last()
    ll.print_content()
