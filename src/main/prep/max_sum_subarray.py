
arr = [-2, -5, -3, -4, -8, -1, -2, -11, -5, -4]
#arr = [34, -50, 42, 14, -5, 86]
#arr = [2, -8, 3, -2, 4, -10]

cs = arr[0]
ms = arr[0]

cpath = []
cpath.append(arr[0])

mpath = []
mpath.append(arr[0])

c1 = 0
c2 = 0

for i in range(1, len(arr)):
    print(ms, cs, arr[i], cpath)

    if cs + arr[i] > arr[i]:
        c1 = 1
        cs = cs+arr[i]
        cpath.append(arr[i])
    else:
        c2 = 1
        cs = arr[i]
        cpath = []
        cpath.append(arr[i])

    if cs>ms:
        ms = cs
        mpath = []
        mpath = cpath.copy()

print(cs, ms, mpath)