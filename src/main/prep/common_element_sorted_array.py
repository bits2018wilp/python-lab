
arr1 = [13, 27, 35, 40, 49, 55, 59]
arr2 = [17, 35, 39, 40, 55, 58, 60]

def bin_search(arr, s, e, k):
    print(s, e)
    if s >= e:
        return -1

    m = (s+e)//2
    if arr[m] == k:
        return m
    if arr[m] < k:
        return bin_search(arr, m+1, e, k)
    else:
        return bin_search(arr, s, m, k)

j = 0
ce =[]
for i in range(len(arr1)):
    k = arr1[i]
    j = bin_search(arr2, j, len(arr2)-1, k)
    print(j)
    if j == -1:
        j = 0
    else:
        ce.append(k)

print(ce)