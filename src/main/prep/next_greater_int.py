
arr = [3, 0, 1]

bool = False
for x in range(len(arr)-1, -1, -1):

    if bool:
        break
    for y in range(x-1, -1, -1):
        if bool:
            break
        if arr[x] > arr[y]:
            t = arr[x]
            arr[x] = arr[y]
            arr[y] = t
            bool = True
            break

print(arr)
