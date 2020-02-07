from src.main.prep.node import Node

def find_node(root, k, count, hashmap):

    if not root:
        return

    find_node(root.left, k, count, hashmap)
    if root.value in hashmap:
        print(hashmap[root.value], root.value)
        return
    else:
        hashmap[k-root.value] = root.value
    find_node(root.right, k, count, hashmap)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(11)
root.right.right = Node(15)

hashmap = {}
find_node(root, 20, 0, hashmap)
print(hashmap)