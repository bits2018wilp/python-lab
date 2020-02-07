from src.main.prep.counter import Counter
from src.main.prep.node import Node


def create_tree():

    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.left = Node(40)
    root.left.right = Node(50)
    return root

head = None
prev = None

def leaf_to_dll(root):

    global head, prev

    if not root:
        return

    if root.left is None and root.right is None:

        if head is None:
            head = root
            prev = root
        else:
            head.next = root
            root.prev = head
            head = head.next
        print(root)

    leaf_to_dll(root.left)
    leaf_to_dll(root.right)


root = create_tree()
leaf_to_dll(root)

while prev:
    print(prev.prev, prev, prev.next)
    prev = prev.next