
arr1 = [4, 5, 7]
arr2 = [1, 3, 6, None, None, None]

j = len(arr1)
i=0
for k in range(j, len(arr2)):
    print(i, k)
    arr2[k] = arr1[i]
    i+=1

i = 0
j = len(arr1)

while j< len(arr2):
    print(arr2, i, j)
    if arr2[j] < arr2[i]:
        t = arr2[j]
        arr2[j] = arr2[i]
        arr2[i] = t
        j+=1
    elif arr2[j] > arr2[i]:
        i+=1
    else:
        i+=1
        j+=1


