
from src.main.prep.node import Node

def enqueue(val, tail):

    node = Node(val)
    if tail is None:
        tail = node
    else:
        tail.next = node
        tail = tail.next
    return tail

def go_for_next(ptr, val):

    while ptr is not None and ptr.value != val:
        ptr = ptr.next
    return ptr

def dequeueAny(head, catptr, dogptr):

    if head.value == catptr.value:
        catptr = go_for_next(catptr.next, 'cat')
    elif head.value == dogptr.value:
        dogptr = go_for_next(dogptr.next, 'dog')

    node = head
    head = head.next
    node.next = None
    return node, head, catptr, dogptr


def dequeueCat(catpointer, head):

    if head == catpointer:
        head = head.next

    node = catpointer.value
    if cat_pointer and cat_pointer.next:
        catpointer.value = catpointer.next.value
        tmp = catpointer.next.next
        catpointer.next = tmp
        catpointer = go_for_next(catpointer, 'cat')
        tmp = None
        return node, head, catpointer
    else:
        if not cat_pointer:
            return None, head, cat_pointer
        else:
            cat_pointer.value= None
            return None, head, cat_pointer

def dequeueDog(dogpointer, head):

    if head == dogpointer:
        head = head.next

    node = dogpointer.value
    if dogpointer and dogpointer.next:
        dogpointer.value = dogpointer.next.value
        tmp = dogpointer.next.next
        dogpointer.next = tmp
        dogpointer = go_for_next(dogpointer, 'dog')
        tmp = None
        return node, head, dogpointer
    else:
        if not dogpointer:
            return None, head, dogpointer
        else:
            dogpointer.value= None
            return None, head, dogpointer


def print_q(head):
    lst = []
    while head:
        lst.append(head.value)
        lst.append(' -> ')
        head = head.next
    print(lst)

cat_pointer = None
dog_pointer = None
headptr= None
tailptr = None

tailptr = enqueue("cat", tailptr)
headptr = tailptr
cat_pointer = tailptr

tailptr = enqueue("dog", tailptr)
dog_pointer = tailptr

tailptr = enqueue("dog", tailptr)
tailptr = enqueue("cat", tailptr)
print_q(headptr)

node, headptr, cat_pointer = dequeueCat(cat_pointer, headptr)
print(node, headptr, cat_pointer)
print_q(headptr)

node, headptr, cat_pointer = dequeueCat(cat_pointer, headptr)
print(node, headptr, cat_pointer)
print_q(headptr)

node, headptr, dog_pointer = dequeueDog(dog_pointer, headptr)
print(node, headptr, dog_pointer)
print_q(headptr)

node, headptr, dog_pointer = dequeueDog(dog_pointer, headptr)
print(node, headptr, dog_pointer)
print_q(headptr)

tailptr= enqueue('cat', tailptr)
print_q(headptr)