
from src.main.prep.node import Node

def create_tree():

    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(25)
    return root

def get_nodes_in_range(root, l, h, lst):

    print(root, l, h)
    if not root:
        return

    if root.value > l :
        get_nodes_in_range(root.left, l, h, lst)

    if root.value < h:
        get_nodes_in_range(root.right, l, h, lst)

    if root.value >=l and root.value <=h:
        lst.append(root)

root = create_tree()
lst = []
get_nodes_in_range(root, 15, 20, lst)
print(lst)
