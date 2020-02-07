
words = ['apple', 'dog', 'docat', 'fish', 'fiash', 'apricot']

map = {}

def prepare_prefix_map(prefix_len, map, words):
    print(words)
    for i in range(len(words)):

        w = words[i]
        c = w[0:prefix_len]
        if c not in map.keys():
            map[c] = [w]
        else:
            l = map[c]
            l.append(w)

bool = True
length = 1
while bool:

    map = {}
    prepare_prefix_map(length, map, words)
    tmp = []

    for k,v in map.items():
        if len(v) > 1:
           tmp.extend(v)
        else:
            print(k, v)
    if len(tmp) > 0:
        words = []
        words.extend(tmp)
        length+=1
    else:
        bool = False
