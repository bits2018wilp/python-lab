
arr = [0, -1, 2, -3, 1]

def pair_sum(x, arr2):

    # left ->  key
    dict = {}

    for i in arr2:
        if i in dict.keys():
            return i, dict[i]
        else:
            dict[x-i] = i

    return None, None


for z in arr:
    x, y = pair_sum(z, [y for y in arr if y !=z])
    print(x, y, z)