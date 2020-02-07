from src.main.prep.node import Node

root = Node(1)
root.right = Node(2)
root.right.left = Node(4)
root.left = Node(-2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(2)
root.left.right.right = Node(1)

k = 6

def find_path_to_sum(k, root, path):

    if not root:
        return

    path.append(root.value)

    find_path_to_sum(k, root.left, path)
    find_path_to_sum(k, root.right, path)
    print('path: ',path)
    s = 0
    for i in range(len(path)-1, -1, -1):
        s+=path[i]

        if s == k:
            print(path[i:len(path)])
    path.pop()

path = []
find_path_to_sum(k, root, path)
print(path)
