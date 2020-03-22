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
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
print_ll(head)

prev = None
curr = head
next = None
print(prev, curr, next)

i = 1
s = 3
e = 4
s1 = None

while i < s:
    s1 = curr
    curr = curr.next
    i+=1

print(curr, prev, s1)
s2 = curr

while i <= e:

    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    i+=1

print(prev, curr, next, s2)

s1.next = prev
s2.next = curr

print_ll(head)