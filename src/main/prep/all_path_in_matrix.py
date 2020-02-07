
r = 4
c = 4

i = 0
j = 0

paths = []

def find_path(i, j, r, c, path):
    global paths
    if i == r and j == c:
        paths.append(path)
        return

    tmppath = []
    if path is not None:
        tmppath = path.copy()

    if i+1 <= r :
        tmppath.append((i+1, j))
        find_path(i+1, j, r, c, tmppath)

    if j+1 <= c :
        tmppath.append((i, j+1))
        find_path(i, j+1, r, c, tmppath)

path = []
path.append((0,0))
find_path(0, 0, r, c, path)
print(paths)