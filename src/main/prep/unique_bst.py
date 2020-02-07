from src.main.prep.counter import Counter
from src.main.prep.node import Node

def postorder(root, lst):

    if not root:
        return

    lst.append(root)
    postorder(root.left, lst)
    postorder(root.right, lst)


def create_bst(arr, root, tmp):

    if len(arr) == 0:
        return

    if root is None:
        root = Node(arr[0])
        tmp.append(root)
        create_bst(arr[1:], root, tmp)
    else:
        v = arr[0]
        if v <= root.value:
            if not root.left:
                root.left = Node(v)
                create_bst(arr[1:], root, tmp)
            else:
                create_bst( arr, root.left, tmp)
        else:
            if not root.right:
                root.right = Node(v)
                create_bst(arr[1:], root, tmp)
            else:
                create_bst(arr, root.right, tmp)

def unique_comb(arr, lst, lol):

    if len(arr) == 0:
        lol.append(lst)
        return

    for i in range(len(arr)):
        tmp = None
        if lst is None:
            tmp = []
        else:
            tmp = lst.copy()
        a = arr[i]
        tmp.append(a)
        ac = arr.copy()
        ac.remove(a)
        unique_comb(ac, tmp,lol)

n = 3
lol = []
unique_comb([1,2,3], None, lol)

for l in lol:
    #print(l)
    tmp = []
    create_bst(l, None, tmp)
    #print(tmp)
    lst  = []
    postorder(tmp[0], lst)
    print(lst)
