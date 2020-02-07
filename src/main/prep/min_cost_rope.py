
def add_min(arr, lst):

    print(lst, arr)

    if len(arr) == 0 or len(arr) == 1:
        return

    if len(arr)  == 1 :
        t = lst[0]
        lst.remove(t)
        t = t + arr[0]
        lst.append(t)
        return

    i1 = arr[0]
    i2 = arr[1]

    arr.remove(i1)
    arr.remove(i2)

    t = lst[0]
    lst.remove(t)

    t = t + i1+i2

    lst.append(t)
    arr.append(i1+i2)
    arr.sort()

    add_min(arr, lst)


arr = [4, 3, 2, 6]
arr = [4, 2, 7, 6, 9]
arr.sort()
lst = []
lst.append(0)
add_min(arr, lst)
print(lst)