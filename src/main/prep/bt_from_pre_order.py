from src.main.prep.counter import Counter

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

    def __hash__(self):
        return hash(self.value)


def create_tree(nodes, leafs, counter):

    current_val = counter.get_count()

    if current_val == len(nodes):
        return

    node = Node(nodes[current_val])
    counter = counter.increment()

    if leafs[current_val] == 'N':
        node.left = create_tree(nodes, leafs, counter)
        node.right = create_tree(nodes, leafs, counter)

    return node

def preorder(root):

    if not root:
        return

    print(root)
    preorder(root.left)
    preorder(root.right)


nodes = [10, 30, 20, 5, 15]
leafs = ['N', 'N', 'L', 'L', 'L']


# nodes = [10, 30, 20]
# leafs = ['N', 'L', 'L']

root = None
index =  []
index.append(0)
counter = Counter(0)
root = create_tree(nodes, leafs, counter)
print(root)
print(root.left)
print(root.right)

print(root.left.left)
print(root.left.right)
#preorder(root)

