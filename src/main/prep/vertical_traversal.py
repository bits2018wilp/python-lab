
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right  = None
        self.next = None
        self.prev = None
        self.diff = 0
        self.ancestors = []

    def __eq__(self, other):
        return other != None and self.value == other.value and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)


def create_tree():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.left.left = Node(10)
    root.right.right.right = Node(9)

    return root

def create_tree2():

    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    return root

def create_tree3():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.right = Node(7)
    root.right.left = Node(6)
    root.right.left.right = Node(8)

    return root

def preorder_view(root, level, map):

    if not root:
        return

   # print(root,level)
    if map.get(level):
        l = map.get(level)
        l.append(root.value)
    else:
        l = []
        l.append(root.value)
        map[level] = l

    preorder_view(root.left, level+1, map)
    preorder_view(root.right, level+1, map)

def postorder_view(root, level, map):

    if not root:
        return

    postorder_view(root.right, level+1, map)
    postorder_view(root.left, level+1, map)

   # print(root,level)
    if map.get(level):
        l = map.get(level)
        l.append(root.value)
    else:
        l = []
        l.append(root.value)
        map[level] = l


def vertical_view(root, level, map):

    queue = []
    queue.append(root)

    while len(queue) > 0:

        tmpq = queue.copy()
        t = queue[0]
        queue.remove(t)
        print(t)
        if t.left:
            queue.append(t.left)
        if t.right:
            queue.append(t.right)


def max_diff_node_ancestor(root, diff):

    if not root:
        return

    if root.left:
        t = root.left.ancestors + root.ancestors
        t.append(root.value)
        root.left.ancestors.append(max(t))

    if root.right:
        t = root.right.ancestors + root.ancestors
        t.append(root.value)
        root.right.ancestors.append(max(t))

    if len(root.ancestors) >0:
        d = max(root.ancestors)
        if d:
            d = d - root.value
            diff.append(d)

    max_diff_node_ancestor(root.left, diff)
    max_diff_node_ancestor(root.right, diff)

def find_path(root, target,lst):

    if not root:
        return

    if root.value == target:
        root.ancestors.append(root.value)
        lst.extend(root.ancestors)
        #print(root.ancestors)
        return root

    t = root.ancestors.copy()
    t.append(root.value)

    if root.left:
        root.left.ancestors = t

    if root.right:
        root.right.ancestors = t

    find_path(root.left, target, lst)
    find_path(root.right, target, lst)


def print_inorder(root, level):

    if not root:
        return

    print_inorder(root.left, level+1)
    print(root.value, level)
    print_inorder(root.right, level+1)

def find_distance(root, node1, node2):
    lst1 = []
    find_path(root, node1, lst1)
    print(lst1)

    lst2 = []
    find_path(root, node2, lst2)
    print(lst2)

def main():

    # root = create_tree()
    # map1 = {}
    # preorder_view(root, 0, map1)
    # print(map1)
    #
    # map2 = {}
    # postorder_view(root, 0, map2)
    # print(map2)
    #
    # map3 = {}
    # vertical_view(root, 0, map3)
    # print(map3)

    # root = create_tree2()
    # lst = []
    # max_diff_node_ancestor(root, lst)
    # print(lst)

    root = create_tree3()
    find_distance(root, 8, 4)

if __name__ == '__main__':
    main()