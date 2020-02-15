
from src.main.prep.node import Node

def print_ll(h):

    lst = []
    while h:
        lst.append(str(h.value))
        lst.append(' -> ')
        h = h.next
    print("".join(lst))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

k = 2
i = 0
print_ll(head)
tmp = head
rp = None
prev = None

while tmp:

    i+=1

    if i == k+1:
        rp = head
        continue

    if rp and tmp.next:
        rp = rp.next

    prev = tmp
    tmp = tmp.next

print('loop done', rp, prev)
prev.next = head
head = rp.next
rp.next = None
print_ll(head)
