
arr = [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
       ]

ind = [0] * 4
outd = [0] * 4

for i in range(4):
    for j in range(4):

        if arr[i][j] == 1:
            outd[i] += 1
            ind[j] += 1

print(ind)
print(outd)
