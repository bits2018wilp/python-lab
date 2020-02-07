
from src.main.prep.node import Node

def create_tree():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.left.right = Node(6)
    return root

def is_foldable(left, right):
    print(left, right)

    if left and right:
        return is_foldable(left.left, right.right) and is_foldable(left.right, right.left)
    else:
        if left is None and right is None:
            return True
        else:
            return False


def is_foldable_root(root):
    print(is_foldable(root.left, root.right))

root = create_tree()
is_foldable_root(root)

