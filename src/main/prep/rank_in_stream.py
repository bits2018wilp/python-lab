
from src.main.prep.node import Node

#5, 1, 14, 4, 15, 9, 7, 20, 11

root = Node(5)
root.left = Node(1)
root.right = Node(14)
root.left.right = Node(4)
root.right.left = Node(9)
root.right.left.left = Node(7)
root.right.left.right = Node(11)
root.right.right = Node(15)
root.right.right.right = Node(20)

def find_length(root, k, lst):

    if not root:
        lst.append(k)
        return max(lst)

    l = find_length(root.left,k+1, lst)
    r = find_length(root.right, k + 1, lst)
    return max(l, r)

def find_rank(root, key):

    if not root:
        return

    if root.value == key:
        return find_length(root.left, 0, [])
    elif key < root.value:
        return find_rank(root.left, key)
    else:
        return  1 + find_length(root.left, 0, []) + find_rank(root.right, key)

r = find_rank(root, 14)
print(r)