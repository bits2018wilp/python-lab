
# arr1 = [1, 5, 9, 12, 15, 20]
# arr2 = [4, 11, 16, 17]

arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

# arr1 = [10]
# arr2 = [2, 3]

l1 =  arr1[len(arr1)-1]
l2 =  arr2[len(arr2)-1]

print(arr1)
print(arr2)

i = None
j = None

if len(arr1) > len(arr2):
    i = 1
    j = 0
else:
    i = 0
    j = 1

bool = True

while i < len(arr1) and j < len(arr2):

    if arr1[i] > arr2[j]:
        tmp = arr1[i]
        arr1[i] = arr2[j]
        l = j
        for k in range(j+1, len(arr2)):
            if arr2[k] < tmp:
                arr2[k-1] = arr2[k]
                l = k
            else:
                break
        arr2[l] = tmp
        i+=1
#        arr2.sort()
    else:
        tmp = arr2[j]
        arr2[j] = arr1[i]
        l = i
        for k in range(i+1, len(arr1)):
            if arr1[k] < tmp:
                arr1[k-1] = arr1[k]
                l = k
            else:
                break
        arr1[l] = tmp
        j += 1
        #arr1.sort()
    print(arr1, i)
    print(arr2, j)