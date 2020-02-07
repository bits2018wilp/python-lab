class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right  = None
        self.parent = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)


def find_last(root):

    queue = []
    queue.append(root)

    tmp = None
    while len(queue) > 0:

        tmp = queue[0]
#        print('travers: ', tmp)
        queue.remove(tmp)

        if tmp.right is None or tmp.left is None:
            return tmp

        if tmp.right:
            queue.append(tmp.right)
        elif tmp.left:
            queue.append(tmp.left)

    return tmp


def heapify(node):

    if not node :
        return

    if node.left and node.left.value < node.value:
        t = node.value
        node.value = node.left.value
        node.left.value = t
        heapify(node)

    elif node.right and node.right.value < node.value:
        t = node.value
        node.value = node.right.value
        node.right.value = t
        heapify(node)

    elif node.parent and node.value < node.parent.value:
        t = node.parent.value
        node.parent.value = node.value
        node.parent.value = t
        heapify(node.parent)
    else:
        return


def add(node, root):
    #print('adding: ', node)
    last = find_last(root)
    #print('last: ',  last)
    node.parent = last
    if not last.left:
        last.left = node
    else:
        last.right = node

    heapify(node)


def traverse(root):
    print('traversing min heap..')
    queue = []
    queue.append(root)

    while len(queue) > 0:

        tmp = queue[0]
        print(tmp)
        queue.remove(tmp)

        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)


def remove(root):

    last = find_last(root)
    print('last: ', last)
    r = None

    if last.right:
        last = last.right
        last.parent.right = None
        last.parent = None
        r = root.value
        root.value = last.value
        heapify(root)

    if last.left:
        last = last.left
        last.parent.left = None
        last.parent = None
        r = root.value
        root.value = last.value
        heapify(root)

    else:
        r = root.value
        root.value = last.value
        if root.right == last:
            root.right = None
        else:
            root.left = None
        heapify(root)

    print('removed: ', r)

def main():

    root = Node(20)
    add(Node(35), root)
    traverse(root)
    add(Node(18), root)
    traverse(root)
    add(Node(15), root)
    traverse(root)

    remove(root)
    traverse(root)
    remove(root)
    traverse(root)


if __name__ == '__main__':
    main()
