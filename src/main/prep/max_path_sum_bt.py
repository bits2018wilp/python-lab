from src.main.prep.node import Node
from src.main.prep.counter import Counter


def max_sum_path2(root, sum):

    if not root:
        return 0

    if not root.left and not root.right:
        return root.value

    ls = max_sum_path2(root.left, sum)
    rs = max_sum_path2(root.right, sum)

    if root.left and root.right:
        sum.set_count(max(sum.get_count(), ls+rs+root.value))
        return max(ls,rs)+root.value

    if not root.left:
        sum.set_count(max(sum.get_count(), rs+root.value))
        return rs+root.value
    else:
        sum.set_count(max(sum.get_count(), ls+root.value))
        return ls+root.value


def max_sum_path(root, path):

    if not root:
        return

    # if root.left is None and root.right is None:
    #     tmppath = path.copy()
    #     tmppath.append(root.value)
    #     print(tmppath, sum(tmppath))
    # else:
    path.append(root.value)
    max_sum_path(root.left, path)
    max_sum_path(root.right, path)

def for_each_node(root):

    if not root:
        return

    pathl = []
    max_sum_path(root, pathl)
    print(pathl, sum(pathl))
    for_each_node(root.left)
    for_each_node(root.right)

root = Node(-15)
root.left = Node(5)
root.right = Node(6)

root.left.left = Node(-8)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.left.right = Node(1)

root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.right = Node(-1)
root.right.right.right.left = Node(4)
root.right.right.right.right.left = Node(10)

#for_each_node(root)

root2= Node(1)
root2.left = Node(-2)
root2.right = Node(3)
count = Counter(0)
max_sum_path2(root, count)
print(count.get_count())
