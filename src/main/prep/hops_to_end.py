
arr = [2, 0, 1, 0]
#arr = [1, 1, 0, 1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

bool = True

def reach_end(arr, lst, minarr):

    if not arr or len(arr) == 0:
        if len(lst) < len(minarr):
            minarr.clear()
            minarr.extend(lst)
            print(minarr)
        return

    t = arr[0]
    if t == 0 :
        return

    tmplst = []
dsd
    if lst is not None:
        tmplst = lst.copy()
    tmplst.append(t)

    for i in range(1, t+1):
        tmparr = arr[i:]
        reach_end(tmparr, tmplst, minarr)


def reach_end_iter(arr):
    i=0
    while bool:
        print(i)
        if i + arr[i] <= len(arr):
            i += arr[i]

        if i == len(arr)-1:
            print('reached end')
            bool=False
            break

        if arr[i] == 0 and i < len(arr)-1:
            print('not possible')
            break


def minJumps(arr, n):

    if (n <= 1):
        return 0

    # Return -1 if not possible to jump
    if (arr[0] == 0):
        return -1

    maxReach = arr[0]
    step = arr[0]
    jump = 1

    # Start traversing array

    for i in range(1, n):
        # Check if we have reached the end of the array
        if (i == n - 1):
            return jump

            # updating maxReach
        maxReach = max(maxReach, i + arr[i])

        # we use a step to get to the current index
        step -= 1;

        # If no further steps left
        if (step == 0):
            jump += 1
            if (i >= maxReach):
                return -1
            step = maxReach - i;
    return -1

minarr = [0] * len(arr)
reach_end(arr, None, minarr)