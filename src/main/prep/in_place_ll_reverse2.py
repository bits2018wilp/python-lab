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
h2 = None
prev = head
curr = head.next
next = curr.next

print(prev, curr, next)

while next:

    curr.next = prev
    prev = curr
    curr = next
    next = next.next

    print(prev, curr, next)
next = curr
print_ll(curr)
