
mat = [
        [1, 2, 3],
        [4, 6, 5],
        [3, 2, 1]
    ]


def find_path(mat, balance, path, i, j, k):

    if balance <= k and i == 2 and j == 2 :
        print(path)
        return

    if i+1 <= 2 :
        tmppath = None
        if path is None:
            tmppath = []
        else:
            tmppath = path.copy()

        balance1 = balance + mat[i+1][j]
        tmppath.append((i+1, j))
        find_path(mat, balance1, tmppath, i+1, j, k)

    if j+1 <= 2:
        tmppath = None
        if path is None:
            tmppath = []
        else:
            tmppath = path.copy()
        balance2 = balance + mat[i][j+1]
        tmppath.append((i, j+1))
        find_path(mat, balance2, tmppath, i, j+1, k)

balance = mat[0][0]
lst = []
lst.append((0, 0))
find_path(mat, balance, lst, 0, 0, 11)