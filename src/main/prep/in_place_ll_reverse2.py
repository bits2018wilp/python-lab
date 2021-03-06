from src.main.prep.node import Node

def print_ll(h):

    lst = []
    while h:
        lst.append(str(h))
        lst.append("->")
        h = h.next
    print("".join(lst))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print_ll(head)

prev = None
curr = head
next = None

print(prev, curr, next)

while curr:

    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    print(prev, curr, next)

head = prev
print_ll(head)
