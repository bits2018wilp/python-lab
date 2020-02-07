from src.main.prep.node import Node

head = Node(4)
head.next = Node(1)
head.next.next = Node(-3)
head.next.next.next = Node(9)
head.next.next.next.next = Node(2)


head2 = Node(10)
head2.next = Node(80)
head2.next.next = Node(15)
head2.next.next.next = Node(20)
head2.next.next.next.next = Node(40)
head2.next.next.next.next.next = Node(70)
head2.next.next.next.next.next.next = Node(30)

#  4 -> 1 -> -3 -> 9 -> 2

def print_ll(head):
    lst = []
    while head:
        lst.append(str(head.value))
        lst.append(' -> ')
        head = head.next
    return "".join(lst)

def get_tail(start, partition):

    while start and start.next != partition:
        start = start.next

    return start

def partition(start, end) :

    cindex = start
    pivot = end
    if cindex and pivot:
        while cindex:

            if cindex.value < pivot.value:
                t = cindex.value
                cindex.value = start.value
                start.value = t
                start = start.next

            cindex= cindex.next

        t = pivot.value
        pivot.value = start.value
        start.value= t
        return start
    else:
        return None


def quick_sort(start, end, id):

    print(print_ll(start), start, end, id)

    if start and end and start.value != end.value:

        part = partition(start, end)
        if part:
            pp = get_tail(start, part)
            quick_sort(start, pp, 'f')
            quick_sort(part.next, end,'s')


print(print_ll(head2))
quick_sort(head2, head2.next.next.next.next.next.next, None)
print(print_ll(head2))

