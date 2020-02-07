
arr = [5, 8, 9, 11, 12, 15]

arr = [1, 2, 3, 4, 5, 6, 8]

arr = [1, 3, 5, 6, 8, 9, 15]

max_diff = arr[len(arr)-1] - arr[0]

out_loop = True

for x in range(1, max_diff):

    if not out_loop:
        break

    prev = arr[0]
    tmp2 = []
    tmp2.append(prev)
    tmp = arr.copy()
    c = 1

    loop = True
    while loop:

        for i in range(1, len(tmp)):
            if prev + x == tmp[i]:
                prev = tmp[i]
                tmp2.append(prev)
                c+=1
                if  c == 3:
                    break

        if len(tmp2) == 3:
            print(tmp2)

        tmp.remove(tmp[0])
        if len(tmp) < 3:
            loop = False

        tmp2 = []
        prev = tmp[0]
        c=1
        tmp2.append(prev)
