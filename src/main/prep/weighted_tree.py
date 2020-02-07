
from src.main.prep.node import Node

def find_paths_with_single_common_parent(lsts, weight_map):

    for i in range(len(lsts)):
        plst = lsts[i]
        for j in range(i+1, len(lsts)):
            clst = lsts[j]

            p = 0
            q = 0
            cp = 0
            while p < len(plst) and q < len(clst):
                if plst[p].value == clst[q].value:
                    cp+=1
                    p+=1
                    q+=1
                else:
                    break

            if cp == 1:
                p = 0
                w = 0
                while p < len(plst)-1:
                    k = plst[p].value + plst[p+1].value
                    w = w + weight_map[k]
                    p+=1
                p = 0
                while p < len(clst)-1:
                    k = clst[p].value + clst[p+1].value
                    w = w + weight_map[k]
                    p+=1
                print(plst, clst, w)

def find_heaviest_path(root, weight_map, weight_list, lsts):

#    print(root, weight_list)

    if not root:
        print(weight_list)
        return

    children = root.children

    if children is None or len(children) == 0:
        tmp = weight_list.copy()
        tmp.append(root)
        print(tmp)
        lsts.append(tmp)
        return
    else:
        for c in children:
            tmp2 = weight_list.copy()
            tmp2.append(root)
            find_heaviest_path(c, weight_map, tmp2, lsts)


root = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
tmp = []
tmp.append(b)
tmp.append(c)
tmp.append(d)
root.children = tmp

e = Node('e')
f = Node('f')
tmp2 = []
tmp2.append(e)
tmp2.append(f)
d.children = tmp2

g = Node('g')
h = Node('h')
tmp3 = []
tmp3.append(g)
tmp3.append(h)
e.children = tmp3

weight_map = {}
weight_map['ab'] = 3
weight_map['ac'] = 5
weight_map['ad'] = 8
weight_map['de'] = 2
weight_map['df'] = 4
weight_map['eg'] = 1
weight_map['eh'] = 1

lsts = []
find_heaviest_path(root, weight_map, [], lsts)
print(lsts)
find_paths_with_single_common_parent(lsts, weight_map)
