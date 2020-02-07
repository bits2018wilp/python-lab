
from src.main.prep.node import Node

def lock_node(node):

    if not node:
        return

    if not node.left and not node.right:
        return node.lock
    else:
        left_lock = lock_node(node.left)
        right_lock = lock_node(node.right)
        if left_lock == False and right_lock == False:
            node.lock = True
            return True
        else:
            return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(3)

print(lock_node(root))

