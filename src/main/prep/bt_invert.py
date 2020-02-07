
from src.main.prep.node import Node

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')


def invert(root, invertroot):

    if not root:
        return

    invertroot = Node(root.value)
    invertroot.left = invert(root.right, invertroot)
    invertroot.right = invert(root.left, invertroot)

    return invertroot

iroot = invert(root, None)
print(iroot, iroot.left, iroot.right, iroot.left.left, iroot.left.right, iroot.right.left, iroot.right.right)