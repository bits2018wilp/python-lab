
class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right  = None

    def __eq__(self, other):
        return other != None and self.value == other.value and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
n4 = Node(4)

root.left.left = n4
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

# find nodes at same level but with different parents
def find_cousins(parent, root, node, map, level, probe_map):

    #print(map, probe_map)

    if node == root:
        probe_map[level] = parent
        print('found node at ', probe_map)

    if len(probe_map) > 0 and list(probe_map.keys())[0] in map:
        k = list(probe_map.keys())[0]
        v = probe_map[k]
        nn = map[k]
        #print(nn)
        for n in nn:
            if n[0] != v:
                print(n[1])

    nodelist = map.get(level)

    if nodelist == None:
        nodelist = []

    nodelist.append((parent, root))
    map[level] = nodelist

    if root == None:
        return

    find_cousins(root, root.left, node, map, level+1, probe_map)
    find_cousins(root, root.right, node, map, level+1, probe_map)


map = {}
probe_map = {}
find_cousins(None, root, n4, map, 0, probe_map)

#print(map)