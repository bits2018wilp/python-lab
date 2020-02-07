
mat = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
r = 4
c = 4

visited = {}
color = {}
colors_used = []

stack = []
stack.append((0,0))

while len(stack) !=0:

    p = stack.pop()

    if p not in visited:
        visited[p] = 1

        # get adjacent node color in eight direction

        i = p[0]
        j = p[1]

        n1 = (i-1, j)
        n2 = (i+1, j)
        n3 = (i, j-1)
        n4 = (i, j+1)
        n5 = (1-1, j-1)
        n6 = (i-1, j+1)
        n7 = (i+1, j-1)
        n8 = (i + 1, j + 1)

        if i > 0 and mat[i-1][j] == 1:
            stack.append(n1)
        if i < r and mat[i+1][j] ==1:
            stack.append(n2)
        if j > 0 and mat[i][j-1] == 1:
            stack.append(n3)
        if j < c and mat[i][j+1] == 1:
            stack.append(n4)
        if i > 0 and j > 0 and mat[i-1][j-1] == 1:
            stack.append(n5)
        if i > 0 and j < c and mat[i-1][j+1] == 1:
            stack.append(n6)
        if i < r and j > 0 and mat[i+1][j-1] == 1:
            stack.append(n7)
        if i < r and j < c and mat[i+1][j+1] == 1:
            stack.append(n8)

        if mat[i][j] == 1:
            tmpcolors = []
            if n1 in color:
                tmpcolors.append(color[n1])
            if n2 in color:
                tmpcolors.append(color[n2])
            if n3 in color:
                tmpcolors.append(color[n3])
            if n4 in color:
                tmpcolors.append(color[n4])
            if n5 in color:
                tmpcolors.append(color[n5])
            if n6 in color:
                tmpcolors.append(color[n6])
            if n7 in color:
                tmpcolors.append(color[n7])
            if n8 in color:
                tmpcolors.append(color[n8])

            tmpcolors = set(tmpcolors)
            newcolor = None

            for c in colors_used:
                if c not in tmpcolors:
                    newcolor = c
            if newcolor is None:
                if len(colors_used) == 0:
                    newcolor = 1
                    colors_used.append(newcolor)
                else:
                    newcolor = max(colors_used)+1
                    colors_used.append(newcolor)

            color[p] = newcolor

print(colors_used)
print(visited)
print(color)