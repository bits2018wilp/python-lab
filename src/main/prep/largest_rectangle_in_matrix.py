
mat = [ [1, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 0]
     ]

mat = [ [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 1, 1]
     ]

mat = [ [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 1]
     ]


def find_connected_components(mat):

    area = [0] * 4

    for i in range(4):
        for j in range(4):
            if mat[i][j] ==0:
                area[j] = 0
            else:
                area[j] = area[j] + mat[i][j]
        print(area)

        maxx = 0
        localsum = 0
        for k in range(len(area)):
            if area[k] == 0:
                maxx = max(maxx, localsum)
                localsum = 0
            else:
                localsum = localsum + area[k]
        maxx = max(maxx, localsum)
        print(maxx)

find_connected_components(mat)
