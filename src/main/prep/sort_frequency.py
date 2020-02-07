
arr = [1, 1, 2, 2, 4, 5, 6]

def count(arr, x, lst):

    if arr and len(arr) <=1:
        return arr

    mid = int(len(arr)/2)

    if arr[mid] == x:
        lst.append(x)

    arr1 = arr[:mid]
    arr2 = arr[mid:]

    count(arr1, x, lst)
    count(arr2, x, lst)


lst = []
count(arr, 2, lst)
print(lst)