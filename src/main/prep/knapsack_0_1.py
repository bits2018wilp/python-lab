
def find_coins(k, arr):

    if sum(arr) == k:
        print(arr)
        return

    tmparr = arr.copy()
    if sum(tmparr) + 1 <=k:
        tmparr.append(1)
        find_coins(k, tmparr)

    tmparr = arr.copy()
    if sum(tmparr) + 5 <= k:
        tmparr.append(5)
        find_coins(k, tmparr)

    tmparr = arr.copy()
    if sum(tmparr) + 10 <= k:
        tmparr.append(10)
        find_coins(k, tmparr)

    tmparr = arr.copy()
    if sum(tmparr) + 25 <= k:
        tmparr.append(25)
        find_coins(k, tmparr)

find_coins(37, [])