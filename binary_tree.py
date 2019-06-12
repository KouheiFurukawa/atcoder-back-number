class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


class BST:
    def __init__(self, number_list):  # コンストラクタ
        self.root = None  # ルートノード初期化
        for node in number_list:  # 数値を持つ配列から二分木を生成
            self.insert(node)  # 挿入メソッドを使ってノードを挿入する

    def insert(self, data):
        n = self.root
        if n is None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.label
                if data < entry:
                    if n.left is None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif data > entry:
                    if n.right is None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.label = data
                    return

    def search_bool(self, search):
        n = self.root
        if n is None:
            return None
        else:
            lst = [n]
            while len(lst) > 0:
                node = lst.pop()
                if node.label == search:
                    return True
                if node.right is not None:
                    lst.append(node.right)
                if node.left is not None:
                    lst.append(node.left)
            return False


def preorder(node):
    if node is None:
        return
    print(node.label)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.label)
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.label)
