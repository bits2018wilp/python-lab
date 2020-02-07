
matrix =  [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ]


def find_islands(matrix, visited, p, q):

    stack = []
    stack.append((p, q))

    while len(stack) > 0:

        t = stack.pop()
        i = t[0]
        j = t[1]

        if (i, j) not in visited:
            visited.append((i, j))
            print(t)

            if i > 0 and matrix[i-1][j] == 1 and (i-1, j) not in visited:
                stack.append((i-1, j))
            if i < 4 and matrix[i+1][j] == 1 and (i+1, j) not in visited:
                stack.append((i+1, j))
            if j > 0 and matrix[i][j-1] == 1 and (i, j-1) not in visited:
                stack.append((i, j-1))
            if j < 4 and matrix[i][j+1] == 1 and (i, j+1) not in visited:
                stack.append((i, j+1))
            if i > 0 and j > 0 and matrix[i-1][j-1] == 1 and (i-1, j-1) not in visited:
                stack.append((i-1, j-1))
            if i > 0 and j < 4 and matrix[i-1][j+1] == 1 and (i-1, j+1) not in visited:
                stack.append((i-1, j+1))
            if i < 4 and j > 0 and matrix[i+1][j-1] == 1 and (i+1, j-1) not in visited:
                stack.append((i+1, j-1))
            if i < 4 and j < 4 and matrix[i+1][j+1] == 1 and (i+1, j+1) not in visited:
                stack.append((i+1, j+1))


visited = []
def is_connected(arr, x, y):
    global visited
    stack= []
    stack.append((x, y))

    while len(stack) >0:

        t = stack.pop()

        if t in visited:
            continue

        visited.append(t)

        i = t[0]
        j = t[1]
        print(i, j, arr)

        if i <4 and arr[i+1][j] == 1:
            stack.append((i+1, j))

        if i - 1 > 0 and arr[i - 1][j] == 1:
            stack.append((i - 1, j))

        if j + 1 < 5 and arr[i][j + 1] == 1:
            stack.append((i, j+1))

        if j - 1 > 0 and arr[i][j - 1] == 1:
            stack.append((i, j-1))

def find_island2():
    for i in range(5):
        for j in range(5):

            if (i, j) not in visited and matrix[i][j] == 1:
                is_connected(matrix, i, j)

def call_find_island(matrix):
    visited = []

    for i in range(5):
        for j in range(5):

            if (i, j) not in visited and matrix[i][j] == 1:
                print('island at: ', i, j)
                find_islands(matrix, visited, i, j)



call_find_island(matrix)