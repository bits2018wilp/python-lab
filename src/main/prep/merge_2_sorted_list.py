
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
head2.next = Node(9)
head2.next.next = Node(15)

print_ll(head1)
print_ll(head2)

def using_dummy_node(head1, head2):

    dummy = Node(None)
    tail = dummy

    while head1 and head2:
        print(head1, head2, tail, dummy)

        if head1.value <= head2.value:
            tail.next = head1
            tail = tail.next
            head1 = head1.next
        else:
            tail.next = head2
            tail = tail.next
            head2 = head2.next

    while head1:
        tail.next = head1
        tail = tail.next
        head1 = head1.next

    while head2:
        tail.next = head2
        tail = tail.next
        head2 = head2.next

    dummy = dummy.next
    return dummy


def merge(head1, head2):

    temp = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.value <= head2.value:
        temp = head1
        temp.next = merge(head1.next, head2)
    else:
        temp = head2
        temp.next = merge(head1, head2.next)

    return temp

# tmp = merge(head1, head2)
# print_ll(tmp)

dummy = using_dummy_node(head1, head2)
print(dummy)
print_ll(dummy)