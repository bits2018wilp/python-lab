

def can_be_placed(arr, i, j, k):

    for p in range(1, 10):
        if arr[i][p] == k:
            return False

    for q in range(1, 10):
        if arr[q][j] == k:
            return False

    for p in range()

def sudoku_solver(arr, i, j):

    if arr[i][j] == -1:
        tmparr = arr.copy()

        for k in range(1, 10):
            if can_be_placed(k, i, j):
                tmparr[i][j] = k

