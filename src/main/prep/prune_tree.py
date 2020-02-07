
from src.main.prep.node import Node

root = Node(0)
root.left = Node(0)
root.right = Node(0)
root.right.right = Node(0)
root.right.left = Node(0)
root.right.left.right = Node(0)
root.right.left.left = Node(1)

def find_all_zero(node, lst) :

    if not node:
        return

    if node.value == 1:
        lst.append(1)

    find_all_zero(node.left, lst)
    find_all_zero(node.right, lst)

def prune(root, parent, lst):

    if not root:
        return

    tmp = []
    find_all_zero(root, tmp)
    print(tmp)

    if 1 not in tmp:
        if parent:
            if root == parent.left:
                print("pruned left")
                parent.left = None
            else:
                print("pruned right")
                parent.right = None
        else:
            print('root shud be pruned')
            root.left = None
            root.right = None
            return
    else:
        prune(root.left, root, lst)
        prune(root.right, root, lst)

def inorder(root):

    if not root:
        return

    inorder(root.left)
    print(root)
    inorder(root.right)

tmp = []
prune(root, None, tmp)
print('after prune..')
inorder(root)