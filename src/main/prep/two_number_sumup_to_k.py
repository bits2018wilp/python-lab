
arr = [10, 15, 3, 7]
k =17
map = {}

for x in arr:

    if x in map:
        print(x, map[x])
    else:
        map[k-x] = x
