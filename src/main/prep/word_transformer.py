
source = "damp"
target = "like"

lst = ['lamp', 'limp', 'lime']

def find_path(source, target, lst, path):
    print(source, target, path)
   # print(source, path)
    if source == target:
        path.append(target)
        print(path)
        return

    if len(path) == 0:
        path.append(source)

    for i in range(97, 127):

        s = str(chr(i))
        k = 0
        for j in range(0, len(source)):
            tmp = source[0:k] + s + source[j+1:]
            if tmp == target:
                path.append(tmp)
                print(path)
                break
            if tmp in lst and tmp not in path:
                tmppath = path.copy()
                tmppath.append(tmp)
                find_path(tmp, target, lst, tmppath)
            else:
                k+=1

find_path(source, target, lst, [])