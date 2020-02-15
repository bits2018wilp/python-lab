
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

    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value

def inorder(root, lst):

    if not root:
        return

    inorder(root.left, lst)
    lst.append(root)
    inorder(root.right, lst)

def constant_space(root, lst, orig, side):

    if not root:
        return

    constant_space(root.left, lst, orig, 'left')
    if len(lst) == 0:
        lst.append(root)
    else:
        print(lst, root)
        if lst[0] > root and root.value != orig.value:
            print('error node ', root)
        lst.clear()
        lst.append(root)
    constant_space(root.right, lst, orig, 'right')


def constant_space2(root, lst, orig, side):

    if not root:
        return

    constant_space2(root.right, lst, orig, 'right')
    if len(lst) == 0:
        lst.append(root)
    else:
        print(lst, root)
        if lst[0] < root and root.value != orig.value:
            print('error node ', root)
        lst.clear()
        lst.append(root)
    constant_space2(root.left, lst, orig, 'left')


def correct_bst(root, parent, lst, left_or_right):

    if not root:
        return

    correct_bst(root.left, root, lst, 'left')
    if len(lst) == 0:
        lst.append(root)
    else:
        if left_or_right == 'left':
            if lst[len(lst)-1].value > root.value:
                print(lst[len(lst)-1], left_or_right, parent)
        elif left_or_right == 'right':
            print(root, left_or_right, parent)

        lst.append(root)
    correct_bst(root.right, root, lst, 'right')


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


root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(20)
root.right = Node(8)

lst = []
inorder(root, lst)
print(lst)
constant_space(root, [], root, None)
constant_space2(root, [], root, None)

# lst= []
# correct_bst(root, None, lst, None)
# print(lst)

# lst = []
# wrong = []
# find_incorrect_node(root, lst, wrong, True)
# print(lst)
# print(wrong)
