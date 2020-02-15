
arr = [4, 1, 1, 2, 1, 3]
arr = [4, 6, 1, 2, 4, 3]
arr = [4, 6, 1, 2, 1, 3]
# arr = [4, 6, 5, 2, 2, 3]
k = 1

i = 0
j = -1
set = False

while i < len(arr) :

    print(arr, i, j)

    if j == -1 and arr[i] == k:
        j = i

    if j != -1 and i > j and arr[i] != k:
        tmp = arr[j]
        arr[j] = arr[i]
        arr[i] = tmp

        while j < len(arr) and arr[j] != k:
            j+=1

    i+=1
print(arr)
if j == -1:
    print(arr)
else:
    print(arr[0:j])