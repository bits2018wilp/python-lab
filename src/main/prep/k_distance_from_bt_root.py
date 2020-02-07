from src.main.prep.node import Node

def create_tree():

    root = Node(1)
    root.left = Node(2)
    root.right= Node(3)
    root.left.left = Node(4)
    root.left.left.right = Node(8)
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root

def nodes_at_k_distance(root, d, k):

    #print(root, d)
    if not root:
        return

    if d == k:
        print(root)

    nodes_at_k_distance(root.left,  d+1, k)
    nodes_at_k_distance(root.right, d + 1, k)

root = create_tree()
nodes_at_k_distance(root, 0, 2)