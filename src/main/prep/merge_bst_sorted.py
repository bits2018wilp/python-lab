
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

def mins(lst):

    v = 9999
    m = None
    for l in lst:
        if l and l.value <= v:
            m = l
            v = l.value
    return m

def inorder(root, lst):

    if not root:
        return

    inorder(root.left, lst)
    lst.append(root)
    print(root)
    inorder(root.right, lst)

def merge_bst(root1, root2,  lst):

    print('root1inorder: ')
    inorder(root1, lst)
    print('root12inorder: ')
    inorder(root2, lst)
    print('lst: ', lst)

    if not root1 and not root2:
        return

    if not root1:
        inorder(root2, lst)
        return

    if not root2:
        inorder(root1, lst)
        return

    origroot1 = root1
    origroot2 = root2

    p1 = None
    while root1.left:
        p1 = root1
        root1 = root1.left

    p2 = None
    while root2.left:
        p2 = root2
        root2 = root2.left

    if root1.value <= root2.value:
        lst.append(root1)
        if not p1:
            merge_bst(origroot1.right, origroot2, lst)
        else:
            p1.left = root1.right
            merge_bst(origroot1, origroot2, lst)
    else:
        lst.append(root2)
        if not p2:
            merge_bst(origroot1, origroot2.right, lst)
        else:
            p2.left = root2.right
            merge_bst(origroot1, origroot2, lst)


def merge_bst2(root1, root2, stack, lst):

    bool = True
    tmproot1 = root1
    tmproot2 = root2
    leftdone = False

    while bool:

        if not leftdone and tmproot1 and tmproot2:
            if tmproot1.value < tmproot2.value:
                stack.append(tmproot1)
                tmproot1 = tmproot1.left
            else:
                stack.append(tmproot2)
                tmproot2 = tmproot2.left
        else:
            bool = False


    print(stack)

root1 = Node(3)
root1.left = Node(2)
root1.right= Node(5)

root2 = Node(4)
root2.left = Node(1)
root2.right = Node(6)

lst = []
stack = []
merge_bst2(root1, root2, stack, lst)
