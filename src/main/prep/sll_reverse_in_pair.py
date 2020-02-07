
from src.main.prep.node import Node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

n = head.next
c = head
p = None
h = n

def print_ll(h1):
    lst = []
    while h1:
        lst.append(str(h1.value))
        h1 = h1.next
    print(' -> '.join(lst))

p = None
while c:

    if p:
        p.next = n

    t = n.next
    n.next = c
    c.next = t

    p = c
    c = t
    if c:
        n = c.next
    else:
        break


print_ll(h)