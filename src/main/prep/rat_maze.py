
def find_path(mat, i, j, path):

    if i == 3 and j == 3:
        print(path)

    if i == 4 or j == 4:
        return

    if i+1 < 4 and mat[i+1][j] == 1:
        path1 = path.copy()
        path1.append('D')
        find_path(mat, i+1, j, path1)

    if j+1<4 and mat[i][j+1] == 1:
        path2 = path.copy()
        path2.append('R')
        find_path(mat, i, j+1, path2)


mat = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

path = []
find_path(mat,0, 0, path)