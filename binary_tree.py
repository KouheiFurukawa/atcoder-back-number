import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class NewNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.d = None
        self.visited = False

class BST:
    def __init__(self, number_list):
        self.root = None
        for node in number_list:
            self.insert(node)

    def insert(self, data):
        n = self.root
        if n is None:
            self.root = NewNode(data)
            return
        else:
            while True:
                entry = n.data
                if data < entry:
                    if n.left is None:
                        n.left = NewNode(data)
                        n.left.parent = n
                        return
                    else:
                        n = n.left
                elif data > entry:
                    if n.right is None:
                        n.right = NewNode(data)
                        n.right.parent = n
                        return
                    else:
                        n = n.right
                else:
                    n.data = data
                    return

    def search(self, query):
        n = self.root
        while n is not None:
            entry = n.data
            if query < entry:
                n = n.left
            elif query > entry:
                n = n.right
            else:
                return n
        return False

    def successor(self, x):
        xr = x.right
        while xr.left is not None:
            xr = xr.left
        return xr

    def delete_node(self, data):
        z = self.search(data)
        if z.left is None or z.right is None:
            y = z
        else: y = self.successor(z)

        if y.left is not None:
            x = y.left
        else:
            x = y.right

        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        if y != z:
            z.data = y.data

    def inorder(self, n):
        if n is None:
            return
        self.inorder(n.left)
        print(n.data)
        self.inorder(n.right)

tree = BST([6, 3, 7, 1, 4, 8])
q = queue.Queue()
tree.root.d = 0
q.put(tree.root)
distance = 0

while not q.empty():
    temp = q.get()
    print(temp.data, temp.d)
    if temp.left is not None:
        temp.left.d = temp.d + 1
        q.put(temp.left)
    if temp.right is not None:
        temp.right.d = temp.d + 1
        q.put(temp.right)
# tree.inorder(tree.root)