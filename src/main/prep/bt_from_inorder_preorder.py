
from src.main.prep.node import Node

ino = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

preo = ['a', 'b', 'd', 'e', 'c', 'f', 'g']

def create_tree(root, ino):

    global preo

#    print(ino, preo)
    if len(ino) == 0:
        return

    val = preo[0]

    root = Node(val)

    inoi = ino.index(val)
    preo = preo[1:]
    root.left = create_tree(root, ino[0:inoi] )
    root.right = create_tree(root, ino[inoi+1:])

    return root

root  = create_tree(None, ino)

print(root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right)