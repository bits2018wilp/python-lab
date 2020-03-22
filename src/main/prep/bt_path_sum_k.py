
from src.main.prep.node import Node

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.right = Node(4)
root.right.left = Node(9)
root.right.right.right = Node(1)

k = 22

def sum_path(root, lst, k):

    if not root:
        return

    if root:
        tmp = lst.copy()
        tmp.append(root.value)
        if sum(tmp) == k:
            print('sum path: ', tmp)
            return
        else:
            sum_path(root.left, tmp, k)

    if root:
        tmp = lst.copy()
        tmp.append(root.value)
        if sum(tmp) == k:
            print('sum path: ', tmp)
            return
        else:
            sum_path(root.right, tmp, k)

def find_path(root, k):

    llst = []
    llst.append(root.value)
    sum_path(root.left, llst, k)

    rlst = []
    rlst.append(root.value)
    sum_path(root.right, rlst, k)

find_path(root, k)