
arr1 = [1, 5, 9]
arr2 = [7, 5, 98, 0, 2, 1, 3, 5, 9, 9, 1, 1, 5, 8, 8, 91, 7]

map = {}

for i in range(len(arr2)):

    if arr2[i] in arr1:

        lst = map.get(arr2[i])
        if lst is None:
            lst = []
            map[arr2[i]] = lst
        lst.append(i)
        lst.sort()

print(map)

i = 0

lsts = map.values()

while i < len(map.get(5))-1 and len(map.get(9))-1 and len(map.get(1))-1:

    print(map[5][i], map[9][i], map[1][i])
    i+=1
