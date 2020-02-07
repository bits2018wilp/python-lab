
def find_path(n, lists, tgt):

    print(lists)
    if n <= 0:
        return

    if n-1 >= 0:

        list1 = []
        lists.append(list1)

        for l in lists:
            if sum(l) + 1 <= tgt:
                l.append(1)
        find_path(n-1, lists, tgt)


    if n-2 >= 0:
        list2 = []
        lists.append(list2)

        for l in lists:
            if sum(l) + 2 <= tgt:
                l.append(2)
        find_path(n-2, lists, tgt)


lists = []
tgt = 4
find_path(4, lists, tgt)

nl = []
for l in lists:
    if sum(l) == tgt:
        nl.append(l)


print(nl)