
arr = [
       [1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 0, 0],
       [1, 0, 0, 1, 1, 0, 1, 1],
       [1, 2, 2, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 0, 1, 0],
       [1, 1, 1, 2, 2, 2, 2, 0],
       [1, 1, 1, 1, 1, 2, 1, 1],
       [1, 1, 1, 1, 1, 2, 2, 1]
       ]
i = 4
j = 4
nc = 3
old = arr[i][j]
print(arr)

def flood_fill(arr, i, j, nc):

    if i < 0 or j < 0 or i>7 or j > 7:
        return

    if arr[i][j] == old:
        arr[i][j] = nc

        flood_fill(arr, i - 1, j, nc)
        flood_fill(arr, i + 1, j, nc)
        flood_fill(arr, i, j + 1, nc)
        flood_fill(arr, i, j - 1, nc)

flood_fill(arr, i, j, nc)
print(arr)
