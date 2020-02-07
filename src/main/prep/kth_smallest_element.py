
def find_pivot(arr, low, high):
    print(arr, low, high)

    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            t = arr[j]
            arr[j] = arr[i]
            arr[i] = t
    t = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = t
    return i+1, arr


arr = [2, 4, 5, 1, 3, 7, 9, 8, 6]
print(arr)

# pivot , arr = find_pivot(arr, 0, 8)
# print(arr, pivot)

pivot = len(arr)-1

pivot, arr = find_pivot(arr, 0, pivot)
print(arr, pivot)

k = 2
pp = -1

while k-1 != pivot:

    pp = pivot

    if k-1 < pivot:
        pivot, arr = find_pivot(arr, 0, pivot-1)

    else:
        pivot, arr = find_pivot(arr, pivot, len(arr)-1)

    print(arr, pivot)

    # if pp == pivot:
    #     pivot = pivot - 1
