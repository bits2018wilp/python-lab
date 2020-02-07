
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        return other != None and self.value == other.value
               #and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

def serialize(root, lst, level):

    if not root:
        return

    if root.left:
        lst[2 * level + 1] = root.left

    if root.right:
        lst[2 * level + 2] = root.right

    serialize(root.left, lst, level + 1)
    serialize(root.right, lst, level + 1)

def deser(lst, root, level):

    if level >= len(lst):
        return

    root = Node(lst[level])
    root.left = deser(lst, root, 2*level+1)
    root.right = deser(lst, root, 2*level + 2)

    return root

root = Node(20)
root.left = Node(8)
root.right = Node(30)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

lst = [-1] * (pow(2, 4) - 1)

lst[0] = root
print(lst)
serialize(root, lst, 0)
print(lst)
root2 = deser(lst, None, 0)

print(root2, root2.left, root2.right)
print(root2.left.left, root2.left.right)