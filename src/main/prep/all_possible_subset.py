
arr = [1, 2, 3, 5]

def subset(arr, lst):

    print(lst)
    if len(arr) == 0:
        return

    for i in range(len(arr)):

        if lst is None:
            tmplst = []
        else:
            tmplst =lst.copy()

        tmplst.append(arr[i])
        subset(arr[i+1:], tmplst)

subset(arr, None)
