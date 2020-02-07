
from src.main.prep.node import Node
from src.main.prep.counter import Boolean

root = Node(1)
root.left= Node(2)
root.right= Node(3)
root.left.right = Node(4)
root.right.right = Node(5)

root1 = Node(1)
root1.left= Node(2)
root1.right= Node(3)
root1.left.right = Node(4)
root1.right.right = Node(5)

root3 = Node(10)
root3.left = Node(11)
root3.right = Node(21)
root3.left.right = root1

def check_if_same_tree(root1, root2, boolean):

    if root1 and not root2:
        return

    if root2 and not root1:
        return

    if not root1 and not root2:
        boolean.set_value(True)
        return

    if root1.value == root2.value:
        check_if_same_tree(root1.left, root2.left, boolean)
        check_if_same_tree(root1.right, root2.right, boolean)
    else:
        print('mismatch :', root1.value, root2.value)
        boolean.set_value(False)

def check_equality(root, subroot, boolean):

    print(root, subroot)
    if (not root and subroot) or (root and not subroot):
        return

    if root.value == subroot.value:
        if boolean.get_value() is None:
            boolean.set_value(True)
        check_if_same_tree(root, subroot, boolean)
        return
    else:
        if boolean.get_value() == None:
            check_equality(root.left, subroot, boolean)
            check_equality(root.right, subroot, boolean)

boolean = Boolean()
check_equality(root3, root, boolean)
print(boolean)