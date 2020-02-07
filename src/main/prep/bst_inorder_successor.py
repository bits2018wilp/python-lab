from src.main.prep.counter import Object
from src.main.prep.node import Node

def inorder_left(root, obj):

    if not root:
        return

    inorder_left(root.left, obj)
    if obj.get() is None:
        obj.set(root)
    return

def go_up(key, parent, obj):

    if not parent:
        return

    if parent.value > key.value:
        if obj.get() is None:
            obj.set(parent)
            return
    else:
        if parent:
            go_up(key, parent.parent, obj)

def inorder_successor(key):
    print(key)
    if not key:
        return

    if key.right is not None:
        obj = Object()
        inorder_left(key.right, obj)
        return obj
    else:
        obj = Object()
        go_up(key, key.parent, obj)
        return obj

root = Node(50)
root.left = Node(30)
root.left.parent = root

root.left.right = Node(40)
root.left.right.parent = root.left
root.left.right.right = Node(45)
root.left.right.right.parent = root.left.right

root.right = Node(70)
root.right.parent = root

root.right.left = Node(60)
root.right.left.parent = root.right

root.right.left.left = Node(55)
root.right.left.left.parent = root.right.left
root.right.left.right = Node(65)
root.right.left.right.parent = root.right.left

root.right.left.right.right = Node(68)
root.right.left.right.right.parent = root.right.left.right

root.right.right = Node(80)
root.right.right.parent = root.right

root.right.right.left = Node(75)
root.right.right.left.parent = root.right.right

root.right.right.left.right = Node(77)
root.right.right.left.right.parent = root.right.right.left


val = inorder_successor(root.right.left.left)
print(val)
