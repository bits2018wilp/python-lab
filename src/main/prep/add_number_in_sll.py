
from src.main.prep.node import Node

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

head2 = Node(8)
head2.next = Node(9)
head2.next.next = Node(8)
head2.next.next.next = Node(6)
head2.next.next.next.next = Node(7)

head3 = None
remainder = 0
tmp = None
prev = 0
while head1 and head2:
    s = head1.value + head2.value + remainder
    prev = s
    print(remainder, s)
    if s >=10:
        remainder = s//10
        s = s%10
    else:
        remainder = 0

    if head3 is None:
        head3 = Node(s)
        tmp= head3
    else:
        head3.next = Node(s)
        head3 = head3.next
    head1 = head1.next
    head2 = head2.next

while head1:
    s = head1.value + remainder
    prev = s
    if s >=10:
        remainder = s // 10
        s = s % 10
    else:
        remainder =0
    if head3 is None:
        head3 = Node(s)
        tmp = head3
    else:
        head3.next = Node(s)
        head3 = head3.next
    head1 = head1.next

while head2:
    s = head2.value + remainder
    prev = s
    if s >=10:
        remainder = s // 10
        s = s % 10
    else:
        remainder =0
    if head3 is None:
        head3 = Node(s)
    else:
        head3.next = Node(s)
        head3 = head3.next
    head2 = head2.next
head3.value = prev
while tmp:
    print(tmp.value)
    tmp = tmp.next