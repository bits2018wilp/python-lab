
def max_possible_amount(arr, lst1, lst2, turn):

    if len(arr) == 0:
        print(lst1)
        print(lst2)
        return

    f = arr[0]
    l = arr[len(arr)-1]

    if turn:
        turn = False

        tmplst1 = None
        if lst1 is None:
            tmplst1 = []
        else:
            tmplst1 = lst1.copy()

        tmplst1.append(f)
        arr1 = arr.copy()
        arr1.remove(f)
        max_possible_amount(arr1, tmplst1, lst2, turn)

        tmplst2 = None
        if lst1 is None:
            tmplst2 = []
        else:
            tmplst2 = lst1.copy()
        tmplst2.append(l)
        arr1 = arr.copy()
        arr1.remove(l)
        max_possible_amount(arr1, tmplst2, lst2, turn)
    else:
        turn = True

        tmplst1 = None
        if lst2 is None:
            tmplst1 = []
        else:
            tmplst1 = lst2.copy()
        arr1 = arr.copy()
        tmplst1.append(f)
        arr1.remove(f)
        max_possible_amount(arr1, lst1, tmplst1, turn)

        tmplst2 = None
        if lst2 is None:
            tmplst2 = []
        else:
            tmplst2 = lst2.copy()
        arr1 = arr.copy()
        tmplst2.append(l)
        arr1.remove(l)
        max_possible_amount(arr1, lst1, tmplst2, turn)


max_possible_amount([100, 8, 15, 3, 7, 90], None, None, True)