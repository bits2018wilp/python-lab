
arr = [10, 2, 3, 4, 5, 9, 7, 8]

def find_quadruple(arr, lst, k):

    if lst and len(lst) == 4:
        #print(lst)
        if sum(lst) == k:
            print(lst)
        return

    for x in arr:

        tmplst = None
        if lst is None:
            tmplst = []
        else:
            tmplst = lst.copy()

        if len(tmplst) < 4 and sum(tmplst) + x <= k:
            tmplst.append(x)
            tmparr = arr.copy()
            tmparr.remove(x)
            find_quadruple(tmparr, tmplst, k)


find_quadruple(arr, None, 23)
