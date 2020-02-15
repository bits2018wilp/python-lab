
from src.main.prep.node import Node

def print_ll(h):
    lst = []
    while h:
        lst.append(h)
        h = h.next
    print(lst)

head1 = Node(5)
head1.next = Node(8)
head1.next.next = Node(10)

head2 = Node(4)
head2.next = Node(11)
head2.next.next = Node(15)

print_ll(head1)
print_ll(head2)
tmp1 = head1
tmp2 = head2
h2 = None

while tmp1 and tmp2:

    if tmp1 < tmp2:
        if not h2:
            h2 = tmp1
        t = tmp1.next
        tmp1.next = tmp2
        tmp1 = t
        #tmp2 = tmp2.next
    else:
        if not h2:
            h2 = tmp2
        t = tmp2.next
        tmp2.next = tmp1
        #tmp1 = tmp1.next
        tmp2 = t

    print(tmp1, tmp2)
    print_ll(h2)

print(tmp1, tmp2)
print_ll(h2)
