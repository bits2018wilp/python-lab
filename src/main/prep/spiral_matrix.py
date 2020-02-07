
mat = [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
      ]

def print_spiral(mat):

    i = 0
    j = 0

    rs = 0
    re = 3
    cs = 0
    ce = 4

    while True:

        if cs == 4 and rs == 3:
            print('at1')
            break

        while j <= ce:
            print('col: ', mat[i][j])
            j+=1
        j-=1
        ce-=1
        i+=1

        if cs == 4 and rs == 3:
            print('at2')
            break

        while i <= re:
            print('row: ',mat[i][j])
            i+=1

        i-=1
        re-=1
        j-=1

        if cs == 4 and rs == 3:
            print('at3')
            break

        while j >= cs:
            print('colb: ',mat[i][j])
            j-=1

        cs+=1
        j+=1
        i-=1
        rs+=1

        if cs == 4 and rs == 3:
            print('at4')
            break

        while i >= rs:
            print('rowu: ',mat[i][j])
            i-=1
        j+=1
        i+=1

        if cs == ce:
            print('at5')
            break

        print(i, j, cs, ce, rs, re)

print_spiral(mat)