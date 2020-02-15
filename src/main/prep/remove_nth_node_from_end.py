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
head1.next.next.next = Node(12)
head1.next.next.next.next = Node(20)
head1.next.next.next.next.next = Node(30)

k = 3
print_ll(head1)
i=0
ptr = None
tmp = head1

while tmp:
    tmp = tmp.next
    i+=1

    if i == k+1:
        ptr = head1
        continue

    if ptr:
        ptr = ptr.next

print(ptr)
ptr.next = ptr.next.next
print_ll(head1)
