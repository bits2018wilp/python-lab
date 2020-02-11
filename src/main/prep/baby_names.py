
names = {}

names['john'] = 15
names['jon'] = 12
names['johan'] = 20
names['chris'] = 13
names['kris'] = 4
names['christopher'] = 12
names['kasif'] = 12

synonyms = [('jon', 'john'), ('chris', 'kris'), ('johnies', 'johan'), ('chris', 'christopher'), ('johan', 'jon')]

def merge(syns):

    lol = []
    merged = False

    for s in syns:

        if len(lol) == 0:
            tmp = []
            tmp.extend(s)
            lol.append(tmp)
        else:
            found = False
            for l in lol:
                if not found:
                    for e in s:
                        if e in l:
                            l.extend(s)
                            found = True
                            merged = True
                            break
            if not found:
                tmp = []
                tmp.extend(s)
                lol.append(tmp)
        #print(lol)
    return lol, merged

lol, merged = merge(synonyms)
print(lol)
while merged:
    lol, merged = merge(lol)
    print(lol)

map = {}
for i in range(len(lol)):
    map[i] = 0

maxi = i+1

for k, v in names.items():

    found = False
    for i in range(len(lol)):

        if k in lol[i]:
            c = map.get(i)
            c=c+v
            map[i] = c
            found= True

    if not found:
        map[maxi] = v
        maxi+=1

print(map)
