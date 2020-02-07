
def min_jump(arr, lst, i):

    if len(arr) == 0 or len(arr) == 1:
        return

    tmplst = None
    if lst is None:
        tmplst = []
    else:
        tmplst = lst.copy()

    for j in range(1,  arr[i]):
        if i+j <= len(arr):
            tmplst.append(arr[i])
            print(tmplst, arr[j:], i, j)
            if i+j >= len(arr):
                min_jump([], tmplst, j)
            else:
                min_jump(arr[j:], tmplst, j)

arr = [1, 2, 1, 5]
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
lst = []
lst.append(arr[0])
min_jump(arr[1:], lst, 0)