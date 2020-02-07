
from src.main.prep.node import Node

def create_tree():

    root = Node('+')
    root.left = Node('*')
    root.right = Node('-')
    root.left.left = Node(5)
    root.left.right = Node('-')
    root.left.right.left = Node(30)
    root.left.right.right = Node(50)
    root.right.left = Node(100)
    root.right.right = Node(20)
    return root

def evaluate_exp_tree(root, lst, digits, operators, rol):

    if not root:
        return

    if root.left:
        lst.append('(')
    evaluate_exp_tree(root.left, lst, digits, operators, False)
    lst.append(str(root.value))
    evaluate_exp_tree(root.right, lst, digits, operators, True)
    if rol:
        lst.append(')')

digits = [0,1,2,3,4,5,6,7,8,9]
operators = ['+', '-', '*', '/']
lst = []
root = create_tree()
evaluate_exp_tree(root, lst, digits, operators, None)
print(''.join(lst))