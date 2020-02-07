
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

def find_incorrect_node(root, lst, wrong, l):

    if not root:
        return

    if root.left:
        find_incorrect_node(root.left, lst, wrong, True)

    if len(lst) == 0:
        lst.append(root)
    else:
        if root.value > lst[len(lst)-1].value:
            lst.append(root)
        else:
            if l:
                t = lst[len(lst)-1]
                wrong.append(t)
                lst.append(root)
            else:
                wrong.append(root)
                lst.append(root)
    if root.right:
        find_incorrect_node(root.right, lst, wrong, False)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)

lst = []
wrong = []

find_incorrect_node(root, lst, wrong, True)
print(lst)
print(wrong)
