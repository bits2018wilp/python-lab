from src.main.prep.node import Node

# 1 -> 2 -> 3 -> 2 -> 1

def print_ll(h1):
    lst = []
    while h1:
        lst.append(str(h1.value))
        h1 = h1.next
    print(' -> '.join(lst))

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(1)
head.next.next.next.next.next.next.next = Node(1)
print_ll(head)

fast = head
slow = None

while fast:

    fast = fast.next
    if fast:
        fast = fast.next
    if not slow:
        slow = head
    else:
        slow = slow.next

print(fast, slow)
prev = None
curr = slow.next
next = None

while curr:

    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

slow.next = prev
print_ll(head)
print(slow)
p = slow.next
while p:

    if p.value == head.value:
        p = p.next
        head = head.next
    else:
        print('not a plaindrome')
        break
