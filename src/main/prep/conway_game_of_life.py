
mat = [
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0]
    ]


def get_expected_value(islive, live, cv):

    if islive:
        if live < 2:
            return 0
        elif live ==2 or live ==3:
            return 1
        elif live > 3:
            return 0
    else:
        if live == 3:
            return 1
    return cv

def find_live_nearby(i, j, mat):

    live = 0

    if i > 0:
        live = live + mat[i-1][j]
    if j > 0:
        live = live + mat[i][j-1]
    if i < 3:
        live = live + mat[i+1][j]
    if j < 5:
        live = live + mat[i][j+1]
    if i > 0 and j > 0:
        live = live + mat[i-1][j - 1]
    if i < 3 and j > 0:
        live = live + mat[i + 1][j - 1]
    if i < 3 and j < 5:
        live = live + mat[i + 1][j + 1]
    if i > 0 and j < 5:
        live = live + mat[i - 1][j + 1]
    return live

print(mat)
for i in range(4):
    for j in range(6):
        print(i, j)
        live = find_live_nearby(i, j, mat)
        ev = get_expected_value( (mat[i][j]==1), live, mat[i][j])
        print(ev)
        mat[i][j] = ev
        print(mat)