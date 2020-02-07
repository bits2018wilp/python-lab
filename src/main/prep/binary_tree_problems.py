
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right  = None
        self.next = None
        self.prev = None
        self.diff = 0

    def __eq__(self, other):
        return other != None and self.value == other.value and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# #
# n4 = Node(4)
# root.left.left = n4
# root.left.right = Node(5)
# #
# root.right.left = Node(6)
# root.right.right = Node(7)

# root.left.left.left = Node(8)
# root.left.left.right = Node(9)
# #
#
# root.left.right.left = Node(10)
# root.left.right.right = Node(11)
# #
# root.right.left.left = Node(12)
# root.right.left.right = Node(13)
# #
# root.right.right.left = Node(14)
# root.right.right.right = Node(15)

# root.right.right.right = Node(8)
# root.right.right.right.left = Node(9)

root = Node(80)
root.left = Node(49)
root.right = Node(50)
root.left.left = Node(100)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(3)

def left_view(node, dict, level):

    if not node:
        return

    if level not in dict.keys():
        print(node)
        dict[level] = node

    left_view(node.left, dict, level+1)
    left_view(node.right, dict, level + 1)

def right_view(node, dict, level):

    if not node:
        return

    if level not in dict.keys():
        print(node)
        dict[level] = node

    right_view(node.right, dict, level + 1)
    right_view(node.left, dict, level + 1)


def top_view(node, dict, level):

    left_view(node, dict, level)
    dict = {}
    level =0
    right_view(node, dict, level)

def max_value_each_level(node, dict , level):

    if not node:
        return

    if level in dict.keys():
        if dict[level] < node.value:
            dict[level] = node.value
    else:
        dict[level] = node.value

    max_value_each_level(node.left, dict, level+1)
    max_value_each_level(node.right, dict, level + 1)

head = Node(-1)
def convert_to_dll(node):

    global head
    #print(node)
    if not node:
        return

    convert_to_dll(node.left)
    #print(node)
    head.next = node
    head = head.next
    convert_to_dll(node.right)


def max_diff_between_node_ancestor(node, maxv):

    if not node:
        return

    if node.left:
        d = node.value - node.left.value
        s = d + node.diff
        node.left.diff = s
        if s > maxv[0]:
            maxv.clear()
            maxv.append(s)

    if node.right:
        d = node.value - node.right.value
        s = d + node.diff
        node.right.diff = s
        if s > maxv[0]:
            maxv.clear()
            maxv.append(s)

    max_diff_between_node_ancestor(node.left, maxv)
    max_diff_between_node_ancestor(node.right, maxv)


def print_inorder(node):

    if not node:
        return
    print_inorder(node.left)
    print(node, node.next)
    print_inorder(node.right)


def find_ancestors(root, map, rootpathmap):

    if root is None :
        return

    if root.left is None and root.right is None:
        rootpathmap[root.value] = map.get(root.value)

    nodes = map.get(root.value)
    if nodes is None:
       nodes = []
    if root.value not in nodes:
       nodes.append(root.value)

    if root.left is not None:
        map[root.left.value] = nodes.copy()

    if root.right is not None:
        map[root.right.value] = nodes.copy()

    find_ancestors(root.left, map, rootpathmap)
    find_ancestors(root.right, map, rootpathmap)


def find_distance_using_lca(map, x, y):

    path1 = map[x]
    path2 = map[y]
    c = 0
    i = abs(len(path1) - len(path2))

    prev = None

    for n1, n2 in zip(path1, path2):
        if n1 == n2:
            prev = n1
        elif n1 != n2:
            c+=2

    print( x, ' -->', y,  ' lca ==> ',prev, ' dist ==> ',c+i)

def vertical_view(root, map):

    if root is None:
        return

    print('root :', root)
    nodes = map.get(root.value)
    if nodes is None:
        nodes = []
        nodes.append(root.value)

    if root.left is not None and root.left.right is not None:
        nodes.append(root.left.right)
        map[root.left.right.value] = nodes.copy()
        print(root.left.right)

    elif root.right is not None and root.right.left is not None:
        nodes.append(root.right.left)
        map[root.right.left.value] = nodes.copy()
        print(root.right.left)

    vertical_view(root.left, map)
    vertical_view(root.right, map)

# map = {}
# rootpathmap = {}
# find_ancestors(root, map, rootpathmap)
# print(map)
# print( rootpathmap)
#
# find_distance_using_lca(map, 4, 6)
# find_distance_using_lca(map, 8, 6)
# find_distance_using_lca(map, 7, 9)
# find_distance_using_lca(map, 5, 9)
# find_distance_using_lca(map, 6, 9)
#
# vv_map = {}
# vertical_view(root, vv_map)
# print(vv_map)

#dict = {}
#left_view(root, dict, 0)
#top_view(root, dict, 0)
#max_value_each_level(root, dict, 0)
#print(dict)

# start = head
# convert_to_dll(root)
# #print(head)
# while start:
#     print(start)
#     start = start.next
# #print_inorder(root)

maxv = []
maxv.append(-999)
max_diff_between_node_ancestor(root, maxv)
print(maxv)
print(root.right.diff)
print(root.right.right.diff)
print(root.right.right.left.diff)