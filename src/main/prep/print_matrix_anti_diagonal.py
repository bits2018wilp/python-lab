
mat = [
        [1,  2,  3,  10],
        [4,  5,  6,  11],
        [7,  8,  9,  12],
        [13, 14, 15, 16]
    ]

print(mat)

bool = True
r = 0
c = 0
maxr = 3
maxc = 3

i = 0
j = 0
t = 0
s = ''
while bool:

    if i >= 0 and i <= maxr and  j >= 0 and j <= maxc:

        #print(mat[i][j], t)
        s = s + str(mat[i][j]) + ' '
        t+=1

        i -=1
        j +=1
    else:
        print(s)
        s = ''

        if c == 0 and r <= maxr:
            r +=1
            c = 0

        elif  c <= maxc:
            r = maxr
            c += 1

        i = r
        j = c

        if c == maxc and r == maxr:
            print(mat[i][j])
            bool = False
