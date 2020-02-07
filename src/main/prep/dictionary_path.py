
start = 'dog'
end = 'cat'
lst = ["dot", "dop", "dat", "cat"]

map = {}
for w in lst:

    for i in range (len(w)):

        v = map.get(i)
        if v:
            v.add(w[i])
            map[i] = set(v)
        else:
            v = []
            v.append(w[i])
            map[i] = set(v)
print(map)

def find_path(start, end, arr, map, path):
    #print(start, map)
    if start == end:
        print(path)
        return

    for k, v in map.items():

        tmp = start
        for c in v:
            if c != tmp[k]:
                tmp = tmp[0:k]+c+tmp[k+1:]
                #print(tmp)
                if tmp in arr:
                    tmpv = v.copy()
                    tmpv.remove(c)
                    tmpmap = map.copy()
                    tmpmap[k] = tmpv
                    tmppath = path.copy()
                    tmppath.append(tmp)
                    find_path(tmp, end, arr, tmpmap, tmppath)

find_path(start, end, lst, map, [])
