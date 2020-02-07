
def coin_change2(denom, amount, lst):

    if lst and sum(lst) >= amount:
        if sum(lst) == amount:
            print(lst)
        return

    for i in range(len(denom)):

        tmplst = None

        if lst is None:
            tmplst = []
        else:
            tmplst = lst.copy()

        if sum(tmplst) - amount <= 0:
            tmplst.append(denom[i])
            coin_change2(denom, amount, tmplst)


def coin_change(amount, denom, lst):

    if amount <= 0:
        if amount == 0:
            t = lst[0]
            lst.remove(t)
            t+=1
            lst.append(t)
        return

    for d in denom:
        tmp = amount - d
        coin_change(tmp, denom, lst)

amount = 3
denom = [4, 5, 6]
lst = []
lst.append(0)

coin_change2(denom, amount, None)