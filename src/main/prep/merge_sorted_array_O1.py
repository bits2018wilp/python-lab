
import math

def merge(arr1, arr2):

    print(arr1)
    print(arr2)

    j = len(arr2) - 1

    while j >= 0:

        i = len(arr1) - 1
        last = arr1[i]
        i -= 1

        while i>=0 and j >=0 and arr1[i] > arr2[j]:
            arr1[i+1] = arr1[i]
            i-=1

        arr1[i+1] = arr2[j]
        arr2[j] = last
        j-=1
        print(arr1)
        print(arr2)
        print(i, j)


arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

arr1 = [1, 2, 5, 8, 10]
arr2 = [0, 4]
#
# arr1 = [2, 3, 5, 8, 10]
# arr2 = [0, 1]
#
# arr1 = [1, 8]
# arr2 = [2, 4, 6, 7, 9]
#
arr1 = [2, 3, 5, 8, 10]
arr2 = [2, 4, 6, 7, 9]
#
# arr1 = [10]
# arr2 = [2,3]
#
# arr1 = [2]
# arr2 = [3,10]
#
# arr1 = [1, 5, 9, 10]
# arr2 = [2, 3, 4, 13]

merge(arr1, arr2)