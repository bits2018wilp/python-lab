
arr = [10, 100, 93, 32, 35, 65, 80, 90, 94, 6]

ans = [None] * len(arr)

for i in range(len(arr)-1, -1, -1):

    mine = 99999
    print(i)
    for j in range(i, len(arr)):

        if arr[j] > arr[i] and  arr[j] < mine:
            mine = arr[j]

    if mine == 99999:
        ans[i] = -1
    else:
        ans[i] = mine

print(ans)
