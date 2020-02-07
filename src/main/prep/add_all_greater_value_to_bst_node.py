
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

def inorder(root):

    if not root:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)

def modify(root, sum_lst):

    if not root:
        return

    modify(root.right, sum_lst)

    root.value = root.value + sum_lst[0]
    while len(sum_lst) >0:
        del sum_lst[0]
    sum_lst.append(root.value)

    modify(root.left, sum_lst)

root = Node(12)
root.left = Node(1)
root.right = Node(15)
root.right.left = Node(10)
root.right.right = Node(20)

sum_lst = []
sum_lst.append(0)

modify(root, sum_lst)
print(root)
print(root.left)
print(root.right)
print(root.right.left)
print(root.right.right)