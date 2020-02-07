
input = "123"

map = {}
map["1"] = ['a','b','c']
map["2"] = ['d','e','f']
map["3"] = ['p','q','r', 's']

def find_combinations(input, map, lst):

    if not input or len(input) == 0:
        print(lst)
        return

    i = input[0]
    values = map[i]

    if len(lst) == 0:
        for v in values:
            lst.append(v)
        find_combinations(input[1:], map, lst)
    else:
        tmplst = lst.copy()
        for v in values:
            for l in lst:
                if l in tmplst:
                    tmplst.remove(l)
                l = l+v
                tmplst.append(l)
        find_combinations(input[1:], map, tmplst)

find_combinations(input, map, [])