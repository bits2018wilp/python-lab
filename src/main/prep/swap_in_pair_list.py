
from src.main.prep.node import Node

def print_ll(h):

    lst = []
    while h:
        lst.append(h)
        h = h.next
    print(lst)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

tmp = head
h2 = head.next
prev = None

while tmp:
    #breakpoint()

    t = tmp.next

    if t:
        if not prev:
            tmp.next = t.next
            t.next = tmp
        else:
            prev.next = t
            tmp.next = t.next
            t.next = tmp
        prev = tmp
        tmp = tmp.next

    print(prev)
    print_ll(h2)