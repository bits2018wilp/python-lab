
arr = [4, 5, 2, 10, 8]
# -1, 4, -1, 2, 2
arr = [3, 2, 1]
arr = [3,1,5,2,8]
left = [None] * 5


left[0] = -1

for j in range(1, len(arr)):

    if arr[j-1] < arr[j]:
        if left[j-1] != -1:
            left[j] = min(left[j-1], arr[j-1])
        else:
            if arr[j-1] < arr[j]:
                left[j] = arr[j-1]
            else:
                left[j] = -1
    else:
        if left[j-1] != -1:
            if left[j-1] < arr[j]:
                left[j] = left[j-1]
            else:
                if arr[j - 1] < arr[j]:
                    left[j] = arr[j - 1]
                else:
                    left[j] = -1
        else:
            left[j] = -1
print(left)