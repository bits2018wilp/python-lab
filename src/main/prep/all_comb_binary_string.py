
s = "10?01?1?"
def all_comb(bs, list):

    if '?' not in bs:
        list.append(bs)
        return

    index = bs.index('?')
    x = bs[:index] + '0' + bs[index + 1:]
    all_comb(x, list)
    y = bs[:index] + '1' + bs[index + 1:]
    all_comb(y, list)


list = []
all_comb(s, list)
print(list)