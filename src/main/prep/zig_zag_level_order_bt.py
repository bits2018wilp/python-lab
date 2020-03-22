from src.main.prep.node import Node

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

queue = []
queue.append(root)
bit = 0

while len(queue) > 0:

    tmp = []

    while len(queue) > 0:

        n = queue[0]
        queue.remove(n)

        print(n)
        if bit:
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)
        else:
            if n.right:
                tmp.append(n.right)
            if n.left:
                tmp.append(n.left)
    queue = tmp
    if bit == 0:
        bit =1
    else:
        bit=0
