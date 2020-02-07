
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


def create_tree():

    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)

    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)

    root.right.right = Node(9)
    root.right.right.left = Node(4)
    return root


def find_half_nodes(root, parent, lst):

    if not root:
        return

    if (root.left and not root.right) or (root.right and not root.left):
        if parent:
            if len(lst) == 0:
                lst.append(1)
            if parent.left == root:
                if root.left:
                    parent.left = root.left
                else:
                    parent.left = root.right
            else:
                if root.left:
                    parent.right = root.left
                else:
                    parent.right = root.right

    find_half_nodes(root.left, root, lst)
    find_half_nodes(root.right, root, lst)

def inorder(root):

    if not root:
        return

    inorder(root.left)
    print(root)
    inorder(root.right)

root = create_tree()
inorder(root)

lst = []
bool = True
while bool :
    find_half_nodes(root, None, lst)
    print('after half nodes')
    inorder(root)
    if len(lst) == 0:
        bool = False
    else:
        lst = []

