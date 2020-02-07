
arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

def dp_sol(arr, lst):

    if len(arr) ==0:
        print(lst)
        return

    for i in range(len(arr)):

        tmplst = []
        if lst is not None:
            tmplst = lst.copy()

        if len(tmplst) == 0:
            tmplst.append(arr[i])
            tmparr = arr[i+1:]
            dp_sol(tmparr, tmplst)
        else:
            if arr[i] > tmplst[len(tmplst)-1]:
                tmplst.append(arr[i])
                tmparr = arr[i+1:]
                dp_sol(tmparr, tmplst)

def nsquare():
    dict = {}
    j=0
    for x in arr:
        tmp_dict = dict.copy()
        found = False
        if len(dict) == 0:
            j+=1
            dict[j] = [x]
            continue
        else:
            for k,v in dict.items():
                if x > max(dict[k]):
                    j += 1
                    tmp_dict[j] = tmp_dict[k].copy()
                    tmp_dict[k].append(x)
                    found = True

            if not found:
                j += 1
                tmp_dict[j] = [x]

        dict = tmp_dict.copy()

dp_sol(arr, None)