
arr = [3, 5, 1, 2, 4]  # number of inversion are 4:  31, 32, 51, 52, 54

arr = [1, 2, 3, 5, 4]  # nu,ber of inversion are 4: 54

arr = [5, 4, 3, 2, 1]  # nu,ber of inversion are 4:  31, 51, 52, 54

arr = [4, 5, 3, 1, 2]  # nu,ber of inversion are 4:  31, 51, 52, 54

#arr = [1, 2, 3, 4, 5]  # nu,ber of inversion are 4:  31, 51, 52, 54

ic = 0

def merge_sort(arr):

    global ic

    if len(arr) > 1:

        m = len(arr)//2

        arr1 = arr[: m]
        arr2 = arr[m : ]

        merge_sort(arr1)
        merge_sort(arr2)

        print('arrays to merge : ', str(arr1),  str(arr2),  str(arr))

        i=j=k=0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i+=1
                k+=1
            else:       # arr2 < arr1
                arr[k] = arr2[j]
                j+=1
                k+=1
                ic = ic + len(arr1)- i

        while i < len(arr1):
            arr[k] = arr1[i]
            i+=1
            k+=1

        while j < len(arr2):
            arr[k] = arr2[j]
            j+=1
            k+=1

        print(' arrf:  ', str(arr), ic)

merge_sort(arr)
print(ic)

