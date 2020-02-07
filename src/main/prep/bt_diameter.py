
md = 0

class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right  = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

root = Node(1)
root.left = Node(2)
root.left.right = Node(4)

root.right = Node(3)
root.right.right = Node(6)

root.right.left = Node(5)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
root.right.left.right.right = Node(9)
root.right.left.right.right.left = Node(10)

def inorder(node):

    if node == None:
        return

    inorder(node.left)
    print(node)
    inorder(node.right)


def leaf_distance(root):
    global  md

    if root == None:
        return 0

    ld = leaf_distance(root.left)
    rd = leaf_distance(root.right)

    cd = ld + rd + 1
    md = max(md, cd)
    return max(ld, rd) + 1


#inorder(root)

list = []
leaf_distance(root)
print(md)

