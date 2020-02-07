
def add(e, arr):
    if len(arr) < 4:
        arr.append(e)
        arr.sort()
        return arr

    tmp = arr + [e]
    tmp.sort(reverse=True)
    arr = tmp[0:4]
    return arr

arr = []

arr  = add(4, arr)
arr  = add(2, arr)
arr  = add(1, arr)
arr  = add(3, arr)
print(arr)
arr = add(5, arr)
print(arr)
