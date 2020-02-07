
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

def check_sum_tree(node):

    if node == None:
        return 0

    elif node.left.value == 0 and node.right.value==0:
        return node.value

    return node.value == (check_sum_tree(node.left) + check_sum_tree(node.right))


root = Node(22)
root.left = Node(9)
root.right = Node(13)

n4 = Node(0)
root.left.left = n4
root.left.right = Node(0)

root.right.left = Node(0)
root.right.right = Node(0)

print(check_sum_tree(root))

