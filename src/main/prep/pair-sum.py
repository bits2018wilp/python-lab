
arr = [8, 7, 2, 5, 3, 1]

print(arr)

s = 10

tmp = []

def sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[len(list) -1] + sum(list[:len(list)-2])

pf = [[]]

for i in arr:
        pair_found = False
        tpf = pf
        for l in pf:
            if l is not None:
                sol = sum(l)
                if sol + i == s:
                    l.append(i)
                    tpf.append(l)
                    pair_found = True
                    break
        if pair_found is False:
            l = []
            l.append(i)
            tpf.append(l)

        pf = tpf

print(pf)