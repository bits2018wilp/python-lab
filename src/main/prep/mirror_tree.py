
from src.main.prep.node import Node

def create_tree():

    node = Node(10)
    node.left = Node(20)
    node.right = Node(30)
    node.left.right = Node(50)
    node.right.left = Node(60)
    return node

def create_mirror(root):

    if not root:
        return

    node = Node(root.value)
    node.left = create_mirror(root.right)
    node.right = create_mirror(root.left)

    return node

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root)
    inorder(root.right)

root = create_tree()
inorder(root)
mirrortree = create_mirror(root)
print('mirror')
inorder(mirrortree)