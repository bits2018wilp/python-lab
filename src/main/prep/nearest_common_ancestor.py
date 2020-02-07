import math
from src.main.prep.node import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

def find_root_to_node_path(root, node, path):

    if not root:
        return

    if root.value == node.value:
        return

    path.append(root)
    find_root_to_node_path(root.left, node, path)
    find_root_to_node_path(root.right, node, path)

def find_ancestor(a, b, root):

    if not root:
        return

    patha = []
    find_root_to_node_path(root, a, patha)

    pathb = []
    find_root_to_node_path(root, b, pathb)

    print(patha)
    print(pathb)

find_ancestor(root.left.left, root.left.right.left, root)