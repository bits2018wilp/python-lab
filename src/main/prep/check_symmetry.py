
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
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
#root.right.right = Node(5)

#root.right.left.right = Node(8)
# root.right.left.right.right = Node(9)
# root.right.left.right.right.left = Node(10)

gb = True
def check_symmetry(l, r):
    global gb

    if (l is None and r is not None) or (l is not None and r is None) :
         gb = False
         return

    if r is None and l is None:
        return

    if (l is not None and r is not None) or (l is None and r is None) :
        gb = (gb & True)
    else:
        gb = (gb & False)

    check_symmetry(l.left, r.right)
    check_symmetry(l.right, r.left)

check_symmetry(root.left, root.right)
print(gb)