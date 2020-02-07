
from src.main.prep.node import Node

def create_tree():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(5)
    return root

def get_sum_at_odd_even_level(root, level, olst, elst):

    if not root:
        return

    if level%2 == 0:
        elst.append(root)
    else:
        olst.append(root)
    get_sum_at_odd_even_level(root.left, level+1, olst, elst)
    get_sum_at_odd_even_level(root.right, level + 1, olst, elst)

root = create_tree()
olst = []
elst = []
get_sum_at_odd_even_level(root, 1, olst, elst)
print(olst, elst)