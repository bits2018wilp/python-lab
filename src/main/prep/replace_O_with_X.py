
matrix = [
        ['X', 'O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X', 'O', 'X'],
        ['X', 'X', 'X', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'X', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O']
]

old = 'O'
nc = 'K'

def flood_fill(arr, i, j, nc):

    if i < 0 or j < 0 or i > 5 or j > 5 or arr[i][j] != old:
        return

    if arr[i][j] == old:
        arr[i][j] = nc

        flood_fill(arr, i - 1, j, nc)
        flood_fill(arr, i + 1, j, nc)
        flood_fill(arr, i, j + 1, nc)
        flood_fill(arr, i, j - 1, nc)

for i in range(0, 6):
        flood_fill(matrix, 0, i, nc)

for i in range(0, 6):
        flood_fill(matrix, 5, i, nc)

for i in range(0, 6):
        flood_fill(matrix, i, 0, nc)

for i in range(0, 6):
        flood_fill(matrix, i, 5, nc)

for i in range(0, 6):
        for j in range(0, 6):
                if matrix[i][j] == 'O':
                        matrix[i][j] = 'X'

for i in range(0, 6):
        for j in range(0, 6):
                if matrix[i][j] == 'K':
                        matrix[i][j] = 'O'

print(matrix)
