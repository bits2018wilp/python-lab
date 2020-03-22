
arr = [1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7]

arr = [1, 1, 3, 3, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 11, 12]
arr = [1,1,2]
i = 1
j = 1
dupe = []

while j < len(arr):

    if i == j and arr[i] != arr[i-1]:
        i+=1
        j+=1
    elif arr[j] == arr[j-1]:
        j+=1
    else:
        arr[i] = arr[j]
        i+=1
        j+=1

print(arr[:i])






