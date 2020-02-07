
arr = [2, 4, 6, 2, 3]

def max_sum_linear_time(arr):

    incl = arr[0]
    excl = arr[1]
    excl_new = None

    for i in range(2, len(arr)):

        excl_new = max(incl, excl)

        excl = incl + arr[i]
        incl = excl_new

    print(max(excl, incl))

max_sum_linear_time(arr)

def get_sum(arr, lst):

    if len(arr) == 0:
        print(lst, sum(lst))
        return

    for i in range(len(arr)):

        tmplst = []
        if lst is not None and len(lst)>0:
            tmplst =  lst.copy()

        t = arr[i]
        if len(tmplst) ==0:
            tmplst.append(t)
            get_sum(arr[i+2:], tmplst)
        else:
            if sum(lst) <0 and t >0:
                tmplst =[]
                tmplst.append(t)
                get_sum(arr[i+2:], tmplst)
            elif sum(lst) + t > sum(lst):
                tmplst.append(t)
                get_sum(arr[i + 2:], tmplst)

get_sum(arr, None)