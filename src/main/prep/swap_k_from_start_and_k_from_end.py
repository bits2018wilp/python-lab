
class Node:

    def __init__(self, val):
        self.value = val
        self.next = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.next == other.next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

def create_ll():

    root = Node(1)
    start = root

    for i in range(2, 12):
        tmp = Node(i)
        start.next = tmp
        start = start.next

    return root

def traverse_ll(start):
    while start:

        print(start)
        start = start.next

def print_k_from_start_and_end(root, k):

    start = root
    hop = 0
    j = 0

    root2 = root
    slowp = root

    is_apart = False
    while root2 and root2.next:

        if j < k:
            start = start.next
            j+=1

        if is_apart:
            slowp = slowp.next
            root2 = root2.next
        elif not is_apart:
            is_apart = True
            for i in range(k):

                if root2:
                    root2 = root2.next
                if j < k:
                    start = start.next
                    j += 1
    print(start, slowp, root2)


def main():
    start = create_ll()
   # traverse_ll(start)
    print_k_from_start_and_end(start, 10)


if __name__ == '__main__':
    main()
