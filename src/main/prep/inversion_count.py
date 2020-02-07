
from src.main.prep.counter import Counter

#arr = [2, 4, 1, 3, 5]
# arr = [5, 4, 3, 2, 1]
arr = [5, 4, 1, 2, 3]
# arr= [3, 1, 2]

def merge_sort(arr, count):

    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    merge_sort(arr1, count)
    merge_sort(arr2, count)

    i = 0
    j = 0
    r = 0
    x = 0

    print('before: ',arr, arr1, arr2, i, j, r, count)
    l1 = 0
    l2 = 0

    while i < len(arr1) and j < len(arr2):

       if arr1[i] <= arr2[j]:
           t = arr1[i]
           arr[r] = t
           l1+=1
           i+=1
           r+=1
       else:
           count.add(len(arr1)-i)
           t = arr2[j]
           arr[r] = t
           l2+=1
           j += 1
           r += 1

    print('after1: ', arr, arr1, arr2, i, j, r, count)

    while i < len(arr1):
        arr[r] = arr1[i]
        r+=1
        i+=1

    while j < len(arr2):
        arr[r] = arr2[j]
        r += 1
        j += 1
    print('after loop: ',arr, arr1, arr2, i, j, r, count)

count = Counter(0)
merge_sort(arr,  count)
print(arr, count)