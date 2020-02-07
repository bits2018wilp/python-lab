
def get_max_color(tmp):

    dict = {}
    for t in tmp:
        if t in dict:
            c = dict[t]
            dict[t] = c+1
        else:
            dict[t] = 1

    m = max(dict.values())
    for k,v in dict.items():
        if v == m:
            return k

arr = [
        ['o','o','o','o','x','x','o'],
        ['o','x','o','x','o','o','x'],
        ['x','x','x','x','o','x','o'],
        ['o','x','x','x','o','o','o']
    ]

arr = [['x', 'x', 'o'], ['o','o','x'], ['o','x','o'], ['o','o','o'], ['x','o','x'], ['x','o','x'], ['o','x','o'],['x','x','o'], ['x','x','x'], ['o', 'o', 'o']]
colors = ['r', 'g', 'b', 'w', 'v', 'y']

maxr = 10
maxc = 3

for i in range(maxr):
    j=0
    l = False
    r = False
    u = False
    d = False
    tmp = []

    while j < maxc:

        if arr[i][j] != 'o':
            print(arr, i, j)

            #left
            if j-1 >= 0 and (arr[i][j-1] == 'x' or arr[i][j-1] != 'o'):
                l = True
                tmp.append(arr[i][j-1])
            if j+1 < maxc and (arr[i][j+1] == 'x' or arr[i][j+1] != 'o'):
                r = True
                tmp.append(arr[i][j+1])
            if i -1 >=0 and (arr[i-1][j] == 'x' or arr[i-1][j] != 'o'):
                u = True
                tmp.append(arr[i-1][j])
            if i+1 < maxr and (arr[i+1][j] == 'x' or arr[i+1][j] != 'o'):
                d = True
                tmp.append(arr[i+1][j])

            tmp = list(filter(('x').__ne__, tmp))

            c = None
            if len(tmp) > 0:
                c = tmp[0]#get_max_color(tmp)
            else:
                c = colors.pop()
            #print(tmp, i,j, c)

            arr[i][j] = c
            if l:
                arr[i][j-1] = c
                l = False
            if r:
                arr[i][j+1] = c
                r =False
            if u :
                arr[i-1][j] = c
                u = False
            if d:
                arr[i+1][j] = c
                d = False
            tmp = []
        else:
            pass
        j+=1

print(arr)