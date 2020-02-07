from src.main.prep.node import Node
from src.main.prep.counter import Counter

def is_bst(root, counter, path):

    if not root:
        return

    if root.left:
        if root.left.value <= root.value:
            is_bst(root.left, counter.increment(), path)
        else:
            return False

    path.append(root)

    if root.right:
        if root.right.value > root.value:
            is_bst(root.right, counter.increment(), path)
        else:
            return False

    return True


def find_largest_bst(root):

    if not root:
        return

    counter = Counter(0)
    pathl = []
    isleftbst = is_bst(root.left, counter, pathl)
    pathr = []
    isrightbst = is_bst(root.right, counter, pathr)

    if isrightbst and isleftbst:
        #pathl.extend(pathr)
        if root.value > root.left.value and root.value < root.right.value:
            print('left and right bst ',root, pathl, pathr)
        else:
            print('left bst ', pathl)
            print('right bst ', pathr)
    else:
        if isleftbst:
            pathl.append(root)
            print('left is bst ',root, pathl)
        else:
            print('find largest bst at ', root.left)
            find_largest_bst(root.left)

        if isrightbst:
            pathr.append(root)
            print('right is bst ',root, pathr)
        else:
            print('find largest bst at ', root.right)
            find_largest_bst(root.right)


root = Node(50)

root.left = Node(20)

node13 = Node(18)
root.left.left = node13
node13.left = Node(8)
node13.left.left = Node(5)
node13.left.left.left = Node(3)
node13.left.right = Node(10)
node13.left.right.left = Node(9)
node13.right = Node(27)
node13.right.right = Node(37)

root.left.right = Node(28)
root.right = Node(75)
root.right.left = Node(65)
root.right.right = Node(85)

find_largest_bst(root)
