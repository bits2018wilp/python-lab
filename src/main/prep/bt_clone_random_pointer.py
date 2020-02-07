
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right  = None
        self.random = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

def create_tree():

    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(5)

    root.random = root.left.right
    root.left.left.random = root
    root.right.random = root.left
    return root

def clone(root, map):

    if not root:
        return

    node = Node(root.value)
    map[node.value] = node
    node.left = clone(root.left, map)
    node.right = clone(root.right, map)

    if root.random:
        n = map[root.random.value]
        node.random = n
    return node

def traverse(root):

    queue = []
    queue.append(root)
    while len(queue) >0:
        t = queue[0]
        queue.remove(t)
        #print(t, t.random)
        if t.left:
            queue.append(t.left)
        if t.right:
            queue.append(t.right)


def main():

    root = create_tree()
    traverse(root)
    map = {}
    clonetree = clone(root, map)
    traverse(clonetree)
    #print(map)

    print(clonetree.random)
    print(clonetree.left.left.random )
    print(clonetree.right.random )
if __name__ == '__main__':
    main()
