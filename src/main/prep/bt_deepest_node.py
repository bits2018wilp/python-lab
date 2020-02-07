
from src.main.prep.node import Node

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')

def find_deepest(root, parent, count):

    if not root:
        print(parent, count)
        return

    find_deepest(root.left, root, count+1)
    find_deepest(root.right, root, count+1)

find_deepest(root, None, 0)