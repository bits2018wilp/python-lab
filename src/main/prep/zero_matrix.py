
arr = [

    [1,0,3, 2],
    [2,1,0, 5],
    [1,2,3, 7]
]
i = 0
rows = []
cols = []
while i < 3:

    j =0
    bool = True
    while j < 3 and bool:

        print('marking')
        if arr[i][j] == 0:
            rows.append(i)
            cols.append(j)
            bool = False
        j+=1
    i+=1


i=0

for i in rows:
    j =0
    while j < 4:
        arr[i][j] = 0
        j+=1

for i in cols:
    j =0
    while j < 3:
        arr[j][i] = 0
        j+=1
print(arr)