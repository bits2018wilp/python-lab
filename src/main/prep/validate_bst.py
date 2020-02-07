
from src.main.prep.node import Node

root = Node(7)

root.left = Node(4)
root.right = Node(11)

root.left.left = Node(3)
root.left.right = Node(6)

root.right.left = Node(10)
#root.right.left.left = Node(12)
root.right.right = Node(15)

def validate_bst(root):

    if not root:
        return

    if root.left:
        if root.left.value <= root.value:
            validate_bst(root.left)
        else:
            raise Exception('invalid bst in left', root.value, root.left.value)

    if root.right:
        if root.right.value > root.value:
            validate_bst(root.right)
        else:
            raise Exception('invalid bst in right', root.value, root.right.value)

validate_bst(root)