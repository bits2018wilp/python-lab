
arr = [ 6, 0, 8, 2, 0, 0, 4, 0, 1 ]

c = 0

for i in range(len(arr)):

    if arr[i] != 0:
        arr[c] = arr[i]
        c+=1
        if i > c:
            arr[i] = 0

print(arr)