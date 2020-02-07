
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.next_right = None

    def __eq__(self, other):
        return other != None and self.value == other.value
               #and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)




root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)

queue = []
queue.append(root)

while len(queue) != 0:

    tmpq = []
    old = None
    for n in queue:
        if old is not None:
            old.next_right = n
        if n.left is not None:
            tmpq.append(n.left)
        if n.right is not None:
            tmpq.append(n.right)
        old = n
    queue = tmpq

print(root.next_right)
print(root.left.next_right)
print(root.left.left.next_right)
print(root.left.right.next_right)
print(root.right.right.next_right)