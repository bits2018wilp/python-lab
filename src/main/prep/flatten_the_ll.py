
class Node:

    def __init__(self, val):
        self.value = val
        self.next = None
        self.down  = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.next == other.next and self.down == other.down

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

def create_ll():

    start = Node(5)
    start.next = Node(10)
    start.next.next = Node(19)
    start.next.next.next = Node(28)

    start.down = Node(7)
    start.down.down = Node(8)
    start.down.down.down = Node(30)

    start.next.down = Node(20)

    start.next.next.down = Node(22)
    start.next.next.down.down = Node(50)

    start.next.next.next.down = Node(35)
    start.next.next.next.down.down = Node(40)
    start.next.next.next.down.down.down = Node(45)

    return start

def traverse_sort(start):

    print(start)
    lst = []
    lst.append(start.next)
    lst.append(start.down)

    while len(lst) > 0:
        min = None
        for x in lst:
            if not min:
                min = x
            else:
                if x.value < min.value:
                    min =x
        print(min)
        lst.remove(min)
        if min.next:
            lst.append(min.next)
        if min.down:
            lst.append(min.down)

def main():
    start = create_ll()
    traverse_sort(start)

if __name__ == '__main__':
    main()


