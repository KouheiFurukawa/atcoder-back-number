class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, data_list):
        self.head = None
        for data in data_list:
            self.insert(data)

    def insert_to_head(self, data):
        node = self.head
        self.head = LinkedListNode(data)
        self.head.next = node

    def insert(self, data):
        if self.head is None:
            self.head = LinkedListNode(data)
            return
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = LinkedListNode(data)
        return

    def length(self):
        cnt = 0
        node = self.head
        while node.next is not None:
            cnt += 1
            node = node.next
        return cnt

class PartialSum:
    def __init__(self, node_sum, carry):
        self.node_sum = node_sum
        self.carry = carry


def pad_list(node, n):
    for i in range(n):
        node.insert_to_head(LinkedListNode(0))
    return node


def add_list_helper(n1, n2):
    if n1 is None and n2 is None:
        return PartialSum(None, 0)
    next_sum = add_list_helper(n1.next, n2.next)
    simple_sum = next_sum.carry + n1.data + n2.data
    now_carry = simple_sum // 10
    if next_sum.node_sum:
        return_node = LinkedListNode(simple_sum % 10)
        return_node.next = next_sum.node_sum
        return PartialSum(return_node, now_carry)
    else:
        return PartialSum(LinkedListNode(simple_sum % 10), now_carry)


def add_lists(node1, node2):
    if node1.length() > node2.length():
        node2 = pad_list(node2, node1.length() - node2.length())
    else:
        node1 = pad_list(node1, node2.length() - node1.length())

    result =  add_list_helper(node1.head, node2.head)
    if result.carry == 0:
        return result.node_sum
    else:
        result.node_sum.insert_to_head(1)
        return result.node_sum


if __name__ == '__main__':
    a = SinglyLinkedList([6, 1, 7])
    b = SinglyLinkedList([2, 9, 5])
    c = add_lists(a, b)
    nn = c
    while nn is not None:
        print(nn.data)
        nn = nn.next
