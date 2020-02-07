
s = 'abxaba'
w = 'ab'

def n_square(s, w):

    ws = sorted(w)
    i = 0
    l = len(w)

    while i < len(s):

        tmp = s[i:l+i]
        tmp = sorted(tmp)

        if tmp == ws:
            print(i)

        i+=1

def get_freq_map(w):

    tgtmap = {}
    for c in w:
        if c in tgtmap:
            tgtmap[c] = tgtmap[c] + 1
        else:
            tgtmap[c] = 1
    return tgtmap

def calc_hash(tgtmap):
    hash = 0
    for k,v in tgtmap.items():
        hash = hash + ord(k) * 31 * v
    return hash


def rolling_hash(s, w):

    tgtmap = get_freq_map(w)
    tgthash = calc_hash(tgtmap)

    windowl = len(w)
    i = 0

    while i < len(s):

        tmpmap = {}
        for j in range(i, i+windowl):
            if  j > len(s)-1:
                break
            c = s[j]
            if c in tmpmap:
                tmpmap[c] = tmpmap[c] + 1
            else:
                tmpmap[c] = 1

        tmphash = calc_hash(tmpmap)

        bool = True
        if tgthash == tmphash:
            for k, v in tgtmap.items():
                if tmpmap[k] != v:
                    bool = False
        else:
            bool = False

        if bool:
            print(i)
        i+=1

rolling_hash(s, w)