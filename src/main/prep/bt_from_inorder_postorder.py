
from src.main.prep.node import Node

inord = [2, 1, 3]
postord = [2, 3, 1]

def create_tree(root, inord):
    global postord
    print(inord, postord)
    if not inord or len(inord) == 0:
        return

    val = postord[len(postord)-1]
    root = Node(val)
    index = inord.index(val)

    postord = postord[:len(postord)-1]
    root.right = create_tree(root, inord[index+1:])
    root.left = create_tree(root, inord[:index])

    return root

root = create_tree(None, inord)
print(root, root.left, root.right)