
from src.main.prep.node import Node

def clone(head):

    clonehead = None
    clonehead1 = Node
    tmp = head
    while tmp:
        if clonehead is None:
            clonehead = Node(tmp.value)
            tmp.clonenode = clonehead
            clonehead1 = clonehead
        else:
            clonehead.next = Node(tmp.value)
            clonehead = clonehead.next
            tmp.clonenode = clonehead

        tmp = tmp.next

    # tmp2 = head
    # while tmp2:
    #     print(tmp2, tmp2.clonenode, tmp2.random)
    #     tmp2 = tmp2.next

    tmp = head
    while tmp:
        print(tmp, tmp.clonenode, tmp.random)
        clonednode = tmp.clonenode
        rnode = tmp.random
        if rnode:
            clonednode.random = rnode.clonenode
        #tmp.clonenode = None
        tmp = tmp.next

    tmp2 = clonehead1
    while tmp2:
        print(tmp2 , tmp2.random)
        tmp2 = tmp2.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next.next = Node(5)

head.random = head.next.next
head.next.random = head.next.next.next
head.next.next.next.next.random = head

clone(head)