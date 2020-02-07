
from src.main.prep.node import Node

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

stack = []

while head:
    stack.append(head)
    head = head.next

p = stack.pop()
head = p
while len(stack) > 0:
     e = stack.pop()
     p.next = e
     p = e

p.next = None

t = head
while t:
    print(t)
    t = t.next

c = head
p = None
n = None

while c:

    n = c.next
    c.next = p
    p = c
    c = n

while p:
    print(p)
    p = p.next
