a = [ [1,  2,  3],
      [4,  5,  6],
      [7,  8,  9]
    ]

# 3 6 9
# 2 5 8
# 1 4 7

# 00 01 02      00 10 20
# 10 11 12      01 11 21
# 20 21 22      02 12 22
#
# 02 12 22
# 01 11 21
# 00 10 20

print(a)

for i in range(3):
    for j in range(i):
        t = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = t
print(a)

j=0
for i in range(3):
    t = a[j][i]
    a[j][i] = a[j+2][i]
    a[j+2][i] = t


print(a)
