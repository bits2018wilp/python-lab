from src.main.prep.node import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
# root.right.right= Node(6)
#

def inorder(root, lst):
    if not root:
        return

    inorder(root.left, lst)
    lst.append(root.value)
    lst.append(" -> ")
    inorder(root.right, lst)

def print_arr(head):
    if not head:
        return
    lst = []
    while head:
        lst.append((head.prev, head, head.next))
        head = head.next
    print(lst)

def to_dll(root, head):

    print_arr(head)
    if not root:
        return None

    if root.right:
        head = to_dll(root.right, head)

    if head:
        root.next = head
        head.prev = root

    head = root

    if root.left:
        head = to_dll(root.left, head)

    return head


def to_dll2(root, head):

    if not root:
        return None

    if root.right:
        root.next = to_dll2(root.right, head)

    if not head:
        head = root

    if root.left:
        root.prev = to_dll2(root.left, head)

    return head


lst = []
inorder(root, lst)
print(lst)
head = to_dll(root, None)
print_arr(head)