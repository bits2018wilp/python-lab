
from src.main.prep.node import Node

def create_tree():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    return root

def serialize(root, sbt):

    queue = []
    queue.append(root)

    sbt = str(root.value)
    while len(queue) > 0:

        node = queue[0]
        queue.remove(node)
        if node.left:
            sbt = sbt + ' ' + str(node.left.value)
            queue.append(node.left)
        else:
            if len(queue) > 0:
                sbt = sbt + ' '+str('null')
        if node.right:
            sbt = sbt + ' ' + str(node.right.value)
            queue.append(node.right)
        else:
            if len(queue) > 0:
                sbt = sbt + ' null'
    return sbt

sbt = ''
print(serialize(create_tree(), sbt))