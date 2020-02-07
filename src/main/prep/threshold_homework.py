import math
from src.main.prep.node import Node

arr = [1, 2, 3, 5, 8]
k = 4

arr = [1, 3, 4, 7]
k = 4

# arr = [1, 2, 3, 4]
# k = 4


def find_path(threshold, points, path1, node):

    print(path1)
    if len(points) == 0:
        if max(path1) - min(path1) >= threshold:
            if len(path1) < node.value:
                node.value = len(path1)
        return

    if len(points) > 0:
        tmp = path1.copy()
        tmp.append(points[0])
        find_path(threshold, points[1:], tmp, node)

    if len(points) > 1:
        tmp = path1.copy()
        tmp.append(points[1])
        find_path(threshold, points[2:], tmp, node)


node = Node(9999)
path1 = [arr[0]]
path2 = [arr[0]]
find_path(k, arr[1:], path1, node)
print(path1,  node)