
from src.main.prep.node import Node

def create_tree():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    return root

def is_identical(root1, root2, lst):

    print(root1, root2)
    if not root1 and not root2:
        return

    if root2 and not root1:
        lst.append(False)
    if root1 and not root2:
        lst.append(False)

    if root1.value == root2.value:
        lst.append(True)
        is_identical(root1.left, root2.left, lst)
        is_identical(root1.right, root2.right, lst)
    else:
        lst.append(False)


root1 = create_tree()
root2 = create_tree()
root2.left =Node(9)
lst = []
is_identical(root1, root2, lst)
print(lst)