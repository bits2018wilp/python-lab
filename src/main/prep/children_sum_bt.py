
from src.main.prep.node import Node

def create_tree():

    root = Node(70)
    root.left = Node(20)
    root.right = Node(50)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right.left = Node(23)
    root.right.right = Node(27)
    return root

def check_sum_property(root, lst):

    if not root:
        return 0

    if root.left is None and root.right is None:
        return 0

    if root.value == root.left.value + root.right.value:
        lst.append(True)
        check_sum_property(root.left, lst) and check_sum_property(root.right, lst)
    else:
        lst.append( False)

root = create_tree()
lst = []
check = check_sum_property(root, lst)
print(lst, check)