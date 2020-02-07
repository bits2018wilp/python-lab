
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return other != None and self.value == other.value
               #and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def to_dll(root, prev):

    if not root:
        return
    #print(root, prev)

    if not root.left and not root.right:

        if prev and len(prev) > 0:
            p = prev[0]
            prev.remove(p)
            p.next = root
            root.prev = p
            prev.append(root)
        else:
            prev.append(root)

    to_dll(root.left, prev)
    to_dll(root.right, prev)



def create_tree():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.right = Node(6)
    return root

def main():

    root = create_tree()
    prev = []
    to_dll(root, prev)

    print(root.next)
    print(root.prev)
    print(root.left.next)
    print(root.left.left.next)
    print(root.left.right.prev)
    print(root.left.right.next)
    print(root.right.right.prev)
    print(root.right.right.next)


if __name__ == '__main__':

    main()