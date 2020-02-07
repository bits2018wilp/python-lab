
arr = [5, 8, 6, 2, 3, 4, 6]
#arr = [5, 3, 1, 2, 3, 2]
# 1 3 2 3 2 5
arr.sort()
print(arr)

i = 1
while i< len(arr)-1:
    print(arr)

    if (arr[i] < arr[i-1] and arr[i] < arr[i+1]) or (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
        i+=1
        continue
    elif arr[i] <= arr[i+1] and arr[i]> arr[i-1]:

        t = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = t
    else:
        j = i
        while j < len(arr)-1 and arr[j] == arr[i]:
            j+=1
        t = arr[j]
        arr[j] = arr[i]
        arr[i] = t
    i+=1

print(arr)
