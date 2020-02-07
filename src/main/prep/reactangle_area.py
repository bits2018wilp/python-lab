
arr =[6, 2, 5, 4, 5, 1, 6]


for i in range(1, len(arr)):
    c = 1
    for j in range(i+1, len(arr)):

        if arr[j] >= arr[i]:
            c+=1
        else:
            break

    for j in range(i-1, 0, -1):

        if arr[j] >= arr[i]:
            c+=1
        else:
            break
    print(arr[i], c)
