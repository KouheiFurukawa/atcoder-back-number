from sys import stdin
from binary_tree import BST, inorder, preorder

N = int(stdin.readline().rstrip())
command = [stdin.readline().rstrip() for _ in range(N)]
tree = BST([])

for k in command:
    parsed = k.split()
    print(parsed)
    if parsed[0] == 'insert':
        BST.insert(tree, int(parsed[1]))
    elif parsed[0] == 'print':
        inorder(tree.root)
        preorder(tree.root)

print(BST.search_bool(tree, 88))
