import math
arr = [13, 18, 25, 2, 8, 10]
#arr = [13, 18, 25, 27, 8, 10]
k = 8
#k = 27

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
k = 3

def find_in_rotated_array(k, arr, lo, hi):

    mid = (lo+hi)//2
    print(lo, mid, hi)

    if mid < len(arr) and arr[mid] == k:
        print(mid)
        return
    if lo == hi or lo > hi or mid > len(arr):
      return
    else:
        if (arr[mid-1] > arr[mid] and arr[mid+1] > arr[mid]) or (arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
            if arr[hi] >= k:
                find_in_rotated_array(k, arr, mid+1, hi)
            else:
                find_in_rotated_array(k, arr, lo, mid-1)
        else:
            if k > arr[mid]:
                find_in_rotated_array(k, arr, mid+1, hi)
            else:
                find_in_rotated_array(k, arr, lo, mid-1)



def find_index(k, arr, lo, hi):

    mid = (lo+hi)//2
    print(lo, hi, mid)

    if k == arr[mid]:
        print('found ', k, ' at ', mid)
        return mid
    else:
        if mid+1 < len(arr) and arr[mid+1] < arr[mid]:
            if k < arr[mid] and k <= arr[hi]:
                find_index(k, arr, mid+1, hi)
            else:
                find_index(k, arr, lo, mid-1)
        else:
            print('going in else')
            if k < arr[mid]:
                find_index(k, arr, lo, mid-1)
            else:
                find_index(k, arr, mid+1, hi)

#index = find_index(k, arr, 0, len(arr)-1)
index = find_in_rotated_array(k, arr, 0, len(arr)-1)
print(index)

