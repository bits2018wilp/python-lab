import collections

mat = [ [4, 6, 7],
        [1, 2, 3],
        [4, 5, 6],
        [10, 12, 32]
        ]

print(mat)

def stack_up(od):

    stackup = []
    for k, v in od.items():
        if len(stackup) == 0:
            stackup.append(k)
        else:

            pd = od[stackup[len(stackup)-1]] # last pushed dimension

            maxp = max(pd[1:])
            maxc = max(v[1:])
            if maxc < maxp:
                stackup.append(k)
    print(stackup)
    stackup.sort()
    h = 0
    for s in stackup:
        print(s, od[s])
        h = h + od[s][0]
    print(h)


def stack(fl):

    boxes = {}

    for d in fl:

        base = d[1] * d[2]
        if base not in boxes:
            boxes[base] = d
    print(boxes)
    od = collections.OrderedDict(sorted(boxes.items(), reverse=True))
    print(od)
    stack_up(od)

def all_possible_rotations(arr, lst, fl):

    if len(arr) == 0:
        fl.append(lst)
        return

    for i in range(len(arr)):

        tlst= []
        if lst is None:
            tlst = []
        else:
            tlst = lst.copy()

        tlst.append(arr[i])
        tarr = arr.copy()
        tarr.remove(arr[i])
        all_possible_rotations(tarr, tlst, fl)


fl = []
all_possible_rotations([10, 12, 32], None, fl)
all_possible_rotations([4, 5, 6], None, fl)
all_possible_rotations([4, 6, 7], None, fl)
all_possible_rotations([1, 2, 3], None, fl)
stack(fl)
