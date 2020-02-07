
words = ['bed', 'bath', 'bedbath', 'and', 'beyond']

s = 'bedbathandbeyond'

min = 99999
max = -99999

for w in words:
    l = len(w)

    if l < min:
        min = l
    if l > max:
        max = l
print(min, max)

def create_sentence(s, lst, min, max, i, words):

    if len(s) == 0:
        print(lst)
        return

    tmin = min
    while tmin <= max:
        tmplst = []
        if lst is not None:
            tmplst = lst.copy()
        w = s[i:tmin]
        if w in words:
            tmplst.append(w)
            create_sentence(s[tmin:], tmplst, min, max, 0, words)
        tmin+=1

create_sentence(s, None, min, max, 0, words)