
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

# 1 2 5     1 2 3       1 2 3
# 3 4 6     5 4 6       4 5 6

last = arr1[len(arr1)-1]

i = 0
j = 0

while i < len(arr1) and j < len(arr2):

    if arr1[i] < arr2[j]:
        i+=1
    else:
        arr1[i], arr2[j] = arr2[j], arr1[i]
        if i+1 < len(arr1) and arr1[i] > arr1[i+1]:
            print('sort 1')
            arr1.sort()
        if j+1 < len(arr2) and arr2[j] > arr2[j+1]:
            arr2.sort()
            print('sort 2')
        i+=1

print(arr1)
print(arr2)