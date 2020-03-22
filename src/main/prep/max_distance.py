
arr = [3, 5, 4, 2, 1, 2, 2, 4, 2, 2]

def n_sqr():
    dist_arr = [None] * len(arr)
    j = 0
    # [ 2, 2, 2, -1]

    for k in range(len(arr)):
        b = False
        for i in range(len(arr)-1, k , -1):

            if arr[i] > arr[k]:
                dist_arr[j] = (i-k)
                j+=1
                print(arr[k], arr[i], i)
                b = True
                break
        if not b:
            dist_arr[j] = -1
            j+=1
    print(dist_arr)

def n_log():
    # Python3 implementation of the above approach
    n = 9
    a = [34, 8, 10, 3, 2, 80, 30, 33, 1]

    # To store the index of an element.
    index = dict()
    for i in range(n):
        if a[i] in index:

            # append to list (for duplicates)
            index[a[i]].append(i)
        else:

            # if first occurrence
            index[a[i]] = [i]
    print(index)
    # sort the input array
    a.sort()
    maxDiff = 0

    # Temporary variable to keep track of minimum i
    temp = n
    for i in range(n):
        if temp > index[a[i]][0]:
            temp = index[a[i]][0]
        maxDiff = max(maxDiff, index[a[i]][-1] - temp)

    print(maxDiff)


def maxIndexDiff(arr, n):

    maxDiff = 0;
    LMin = [0] * n
    RMax = [0] * n


    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])

    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1]);

    print(LMin, '\n', RMax)
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        print(maxDiff, i, j, LMin[i], RMax[j])
        if (LMin[i] < RMax[j]):
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1

    return maxDiff

print(maxIndexDiff(arr, len(arr)))