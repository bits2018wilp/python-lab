
arr = [1, 4, 20, 3, 10, 5]

tmparr = []
s = 33
cs = 0

for i in range(len(arr)):

    tmparr.append(arr[i])
    cs =  sum(tmparr)
    print(cs)


    while cs > s:
        tmparr = tmparr[1:]
        cs = sum(tmparr)

    if cs == s:
        break

print(tmparr)
