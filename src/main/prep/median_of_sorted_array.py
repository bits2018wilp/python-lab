import math


def get_median(arr):

    if len(arr)%2 == 0:
        m = len(arr)//2
        return (arr[m] + arr[m+1])/2
    else:
        return arr[math.ceil(len(arr)//2)]

def median(arr1, arr2):

    while len(arr1)>2 and len(arr2)>2:

        m1 = get_median(arr1)
        m2 = get_median(arr2)

        if m1 > m2:

            arr1 = arr1[:math.ceil(len(arr1)//2)+1]
            arr2 = arr2[math.ceil(len(arr2)//2):]
            median(arr1, arr2)
        else:
            arr2 = arr2[:math.ceil(len(arr2) // 2)+1]
            arr1 = arr1[math.ceil(len(arr1) // 2):]
            median(arr1, arr2)

    print(arr1, arr2)
    s = max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])
    return s/2

def median_count(arr1, arr2):

    i = 0
    j = 0
    mc = math.floor((len(arr1) + len(arr2))/2)
    print('mc: ', mc)
    c = 0
    laste = 0
    curre = 0

    while c < mc+1:

        if i < len(arr1):

            if j < len(arr2):

                if arr1[i] < arr2[j]:
                    laste = curre
                    curre = arr1[i]
                    i+=1
                else:
                    laste = curre
                    curre = arr2[j]
                    j+=1
                c+=1
            else:
                laste = curre
                curre = arr1[i]
                i+=1
                c+=1
        else:
            laste = curre
            curre = arr2[j]
            j += 1
            c += 1

    print(c, curre, laste)
    if (len(arr1) + len(arr2))%2 ==0:
        print('median:', (curre+laste)/2)
    else:
        print('medain: ',curre)

arr1 = [1, 2, 5, 8, 10]
arr2 = [0, 4]

arr1 = [2, 3, 5, 8, 10]
arr2 = [0, 1]

arr1 = [1, 8]
arr2 = [2, 4, 6, 7, 9]

arr1 = [2, 3, 5, 8, 10]
arr2 = [2, 4, 6, 7, 9]

arr1 = [10]
arr2 = [2,3]

arr1 = [2]
arr2 = [3,10]

arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

m = median(arr1, arr2)
median_count(arr1, arr2)
print(m)