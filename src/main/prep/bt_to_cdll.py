
from src.main.prep.node import Node
from src.main.prep.counter import Counter

def create_tree():

    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.right.left = Node(36)

    root.left.left = Node(25)
    root.left.right = Node(30)

    return root

def inorder_traverse(root):

    if not root:
        return

    inorder_traverse(root.left)
    print(root)
    inorder_traverse(root.right)
head = None
prev = None

def inorder_to_cdll(root):

    global prev, head

    if root is None:
        return None

    inorder_to_cdll(root.left)

    if prev is None:
        head = root
    else:
        root.prev = prev
        prev.next = root
    prev = root

    inorder_to_cdll(root.right)


root = create_tree()
#inorder_traverse(root)
root = inorder_to_cdll(root)

while head:
    print(head)
    head = head.next

