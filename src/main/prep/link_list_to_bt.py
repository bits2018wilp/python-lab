
from src.main.prep.node import Node
from src.main.prep.counter import Counter


def create_ll():

    head = Node(10)
    tmp = head

    tmp.next = Node(12)
    tmp = tmp.next
    tmp.next = Node(15)
    tmp = tmp.next
    tmp.next = Node(25)
    tmp = tmp.next
    tmp.next = Node(30)
    tmp = tmp.next
    tmp.next = Node(36)
    return head

def print_ll(head):

    while head:
        print(head)
        head = head.next

def get_left(node, counter):

    r = 2 * counter + 1
    for x in range(r):
        if node:
            node = node.next
        else:
            node = None
    return node


def get_right(node, counter):
    r = 2 * counter + 2
    for x in range(r):
        if node:
            node = node.next
        else:
            node = None
    return node

def ll_to_bt(head, i):

    queue = []
    node = Node(head.value)
    queue.append(node)

    while len(queue) > 0:

        tmp = queue[0]
        queue.remove(tmp)
        left = get_left(head, i)
        right = get_right(head, i)
        print(tmp, left, right)
        if left:
            tmp.left = left
            queue.append(left)
        if right:
            tmp.right = right
            queue.append(right)
        i+=1
    return node

head = create_ll()
#print_ll(head)
root = Node(head.value)
root = ll_to_bt( head, 0)
print(root, root.left, root.right, root.left.left, root.left.right, root.right.left)
