
arr = [
        [4, 15, 26],
        [3, 8, 19],
        [1, 11, 13]
    ]

indices = [0] * len(arr)
result = []
completed = []
bool = True

while bool:

    mi = None
    mc =  None
    maxc = 9999
    bool = False

    for i, c in enumerate(indices):
        print(i, c)
        if  c < 3 and arr[i][c] < maxc:
            mc = c
            mi = i
            maxc = arr[i][c]
            bool = True
    print(mi, mc)
    if bool:
        result.append(arr[mi][mc])
        indices[mi] +=1
    print(mi, mc, result)


print(result)