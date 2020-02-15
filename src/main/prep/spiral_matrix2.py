
mat = [
            [1, 2, 3],
            [6, 7, 8],
            [4, 5, 9]
      ]

# 00 01 02 12 22 21 20 10 11
# 00 01 02 03 13 23 22 21 20 10 11 12

# mat = [
#             [1, 2, 3, 12],
#             [6, 7, 8, 16],
#             [61, 71, 81, 161],
#             [4, 5, 9, 65]
#       ]

# mat = [
#             [1, 2, 3],
#             [6, 7, 8],
#             [4, 5, 9],
#             [14, 15, 19],
#             [45, 52, 93]
#       ]

# mat =         [ [1, 2, 3, 4, 5, 6],
#                [7, 8, 9, 10, 11, 12],
#                 [13, 14, 15, 16, 17, 18] ]
minc = 0
minr = 0
maxc = 3
maxr = 3

while minc < maxc and minr < maxr:
    print('loop')

    i = minc
    while i < maxc:
        print('lr ', mat[minr][i])
        i+=1

    minr+=1
    i = minr
    while i < maxr:
        print('bd ',mat[i][maxc-1])
        i+=1


    maxc-=1
    i = maxc-1
    while minr < maxr and i> minc-1:
        print('rl ', mat[maxr-1][i])
        i-=1


    maxr-=1
    i = maxr-1
    while minc < maxc and i > minr-1:
        print('ud ', mat[i][minc])
        i-=1

    minc+=1

    print(minc, maxc, minr, maxr)