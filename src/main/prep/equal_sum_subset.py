
arr = [15, 5, 20, 10, 35, 15, 10]

def find_subset(arr, set1):

    if len(arr) == 0:
        return

    for i in range(len(arr)):

        tmpset = []
        if set1 is not None:
            tmpset = set1.copy()

        tmpset.append(arr[i])

        tmparr = arr.copy()
        tmparr.remove(arr[i])

        if sum(tmpset) == sum(tmparr):
            print(tmpset, tmparr)
            return
        else:
            find_subset(tmparr, tmpset)

find_subset(arr, None)